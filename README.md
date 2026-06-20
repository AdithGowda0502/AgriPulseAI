# 🌾 AgriPulse AI – Real-Time Agricultural Intelligence Platform

## Overview

AgriPulse AI is an end-to-end agricultural intelligence platform that collects live weather data, stores it in SQL Server, analyzes crop information, and generates crop recommendations using Python and Power BI.

---

## Features

- Live Weather Data Integration using Open-Meteo API
- Automated ETL Pipeline using Python
- SQL Server Database Storage
- Crop Analytics Dashboard
- Crop Recommendation Engine
- Power BI Executive Dashboard
- End-to-End Automation Pipeline

---

## Tech Stack

- Python
- SQL Server Express
- SQL Server Management Studio (SSMS)
- Power BI
- Open-Meteo API
- Git & GitHub

---

## Project Architecture

Open-Meteo API
↓
Python ETL
↓
SQL Server
↓
WeatherData
↓
Crop Recommendation Engine
↓
RecommendedCrops
↓
Power BI Dashboard

---

## Modules

### Weather Intelligence

- Current Temperature
- Current Humidity
- Weather Condition
- Temperature Trends
- Humidity Trends

### Crop Analytics

- Market Price Analysis
- Yield Analysis
- Crop Performance Dashboard

### Recommendation Engine

Generates crop recommendations based on current weather conditions.

Example:

Current Temperature: 21.8°C

Recommended Crops:
- Rice
- Wheat
- Sugarcane

---

## Running the Project

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Complete Pipeline

```bash
python scripts/run_agripulse.py
```

---

## Author

Adith K G

Information Science & Engineering

BMS College of Engineering
