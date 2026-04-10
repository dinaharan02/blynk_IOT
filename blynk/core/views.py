import requests
import concurrent.futures
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse


def dashboard(request):
    return render(request, "dashboard.html")


def get_realtime_data(request):
    try:
        urls = {
            "status": f"{settings.BASE_URL}/isHardwareConnected?token={settings.BLYNK_TOKEN}",
            "temp": f"{settings.BASE_URL}/get?token={settings.BLYNK_TOKEN}&v0",
            "hum": f"{settings.BASE_URL}/get?token={settings.BLYNK_TOKEN}&v1",
            "soil": f"{settings.BASE_URL}/get?token={settings.BLYNK_TOKEN}&v2",
        }

        results = {}

        # Parallel API calls (fast)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_key = {
                executor.submit(requests.get, url): key
                for key, url in urls.items()
            }

            for future in concurrent.futures.as_completed(future_to_key):
                key = future_to_key[future]
                results[key] = future.result().text

        is_connected = results["status"] == "true"

        # Default values
        temperature = results["temp"]
        humidity = results["hum"]
        soil_value = int(results["soil"])

        # ✅ SAFE LOGIC (IMPORTANT)
        if not is_connected:
            return JsonResponse({
                "is_connected": False,
                "temperature": None,
                "humidity": None,
                "soil": None,
                "soil_status": "Device Offline"
            })

        # Soil interpretation
        soil_status = "Wet 🌊" if soil_value > 50 else "Dry 🌵"

        return JsonResponse({
            "is_connected": True,
            "temperature": temperature,
            "humidity": humidity,
            "soil": soil_value,
            "soil_status": soil_status
        })

    except Exception as e:
        return JsonResponse({
            "is_connected": False,
            "error": str(e)
        })