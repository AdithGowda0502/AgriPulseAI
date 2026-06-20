import subprocess
import sys
import time

start_time = time.time()

print("🌾 Starting AgriPulse AI Pipeline...\n")

try:
    print("📡 Fetching Weather Data...")
    subprocess.run(
        [sys.executable, "scripts/weather_to_sql.py"],
        check=True
    )

    print("\n🌱 Generating Crop Recommendations...")
    subprocess.run(
        [sys.executable, "scripts/crop_recommendation.py"],
        check=True
    )

    elapsed = round(time.time() - start_time, 2)

    print(f"\n✅ Pipeline Completed Successfully in {elapsed} seconds!")

except subprocess.CalledProcessError as e:
    print("\n❌ Pipeline Failed!")
    print(f"Failed Command: {e.cmd}")

except Exception as e:
    print("\n❌ Unexpected Error!")
    print(str(e))