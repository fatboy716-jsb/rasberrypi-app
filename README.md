# Raspberry Pi Control Board App

A PySide6-based application for controlling and monitoring a Raspberry Pi control board with touchscreen interface.

## Features

- Dark/Light mode toggle
- Temperature unit conversion (Celsius/Fahrenheit)
- Real-time sensor data display
- Touchscreen optimized interface

## Project Structure

```
.
├── assets/         # Static assets (images, icons)
├── fonts/          # Custom fonts
├── responses/      # Response handling
├── screens/        # Screen implementations
├── ui/            # UI files
├── utils/         # Utility functions
├── widgets/       # Custom widgets
├── main.py        # Application entry point
├── settings.py    # Settings management
└── requirements.txt
```

## Setup

1. Install Python 3.8 or higher
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

```bash
python main.py
```

## Controls

- Settings Button: Toggle between Dark and Light mode
- C/F Button: Toggle between Celsius and Fahrenheit temperature display

## Development

The application uses PySide6 for the GUI and pyserial for communication with the control board. The UI is defined in `ui/main_widget_ui.py` and can be modified using Qt Designer. 