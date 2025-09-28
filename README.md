# PyFVCOM - Fixed Version

This is a modified version of PyFVCOM 2.2.0 with critical bug fixes for compatibility with newer Python environments and Windows systems.

## Fixes Applied

This version includes the following critical fixes:

### 1. Matplotlib Import Fix
- **Issue**: `from matplotlib.tri.triangulation import Triangulation` fails in newer matplotlib versions
- **Fix**: Changed to `from matplotlib.tri import Triangulation` in `grid/_grid.py`
- **Files Modified**: `grid/_grid.py`

### 2. SciPy Import Fix  
- **Issue**: `polyfit` and `polyval` were moved from scipy to numpy in newer versions
- **Fix**: Updated imports to use numpy versions in `stats.py`
- **Files Modified**: `stats.py`

### 3. Coordinate Projection String Fix
- **Issue**: Extra comma in UTM projection string causes pyproj errors
- **Fix**: Removed trailing comma in projection format string in `coordinate.py`
- **Files Modified**: `coordinate.py`

### 4. Windows DateTime Compatibility Fix
- **Issue**: `strftime('%s')` is not supported on Windows
- **Fix**: Replaced with `timestamp()` method for cross-platform compatibility
- **Files Modified**: `utilities/time.py`

## Installation

### Option 1: Install from this repository
```bash
pip install git+https://github.com/yourusername/pyFVCOM.git
```

### Option 2: Local installation
```bash
git clone https://github.com/yourusername/pyFVCOM.git
cd pyFVCOM
pip install -e .
```

## Usage

```python
import PyFVCOM as pf
from datetime import datetime

# Create model dates
start = datetime.strptime('2025-5-1', '%Y-%m-%d')
end = datetime.strptime('2025-6-1', '%Y-%m-%d')
interval = 1  # days

# Initialize spherical-grid model preprocessor
model = pf.preproc.Model(start, end, './grid.2dm', 
                        sampling=interval, 
                        native_coordinates='spherical', 
                        zone=20)

# Configure and write output files
model.write_grid('output_grd.dat', depth_file='output_dep.dat')
```

## Compatibility

- **Python**: 3.8+
- **Operating Systems**: Windows, Linux, macOS
- **Dependencies**: Updated to work with current versions of matplotlib, scipy, numpy, and pyproj

## Original PyFVCOM

This is based on PyFVCOM 2.2.0. For the original version and documentation, see:
- Original PyFVCOM: https://github.com/pwcazenave/PyFVCOM

## Contributing

If you find additional issues or improvements, please submit an issue or pull request.

## License

This maintains the same license as the original PyFVCOM project.