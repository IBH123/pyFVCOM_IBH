# Changelog - PyFVCOM Fixed Version

All notable changes to this fixed version of PyFVCOM will be documented in this file.

## [2.2.0-fixed] - 2025-09-28

### Fixed
- **Matplotlib Compatibility**: Fixed import error with `matplotlib.tri.triangulation` module
  - Changed `from matplotlib.tri.triangulation import Triangulation` to `from matplotlib.tri import Triangulation`
  - File: `grid/_grid.py`, line 30

- **SciPy/NumPy Compatibility**: Fixed import errors with polyfit and polyval functions
  - Changed `from scipy import stats, polyfit, polyval` to separate imports
  - Now imports `polyfit, polyval` from numpy instead of scipy
  - File: `stats.py`, line 10

- **Coordinate Projection String**: Fixed UTM projection string formatting error
  - Removed trailing comma in projection format string that caused pyproj errors
  - Changed `"+proj=utm +zone={}, +ellps={} +datum={} +units=m +no_defs"` 
  - To `"+proj=utm +zone={} +ellps={} +datum={} +units=m +no_defs"`
  - File: `coordinate.py`, line 61

- **Windows DateTime Compatibility**: Fixed date formatting issue on Windows
  - Replaced `strftime('%s')` with `timestamp()` method for cross-platform compatibility
  - File: `utilities/time.py`, lines 173-174

### Technical Details

#### Import Fixes
These fixes address changes in newer versions of matplotlib and scipy where certain functions and modules were moved or restructured:

1. **Matplotlib 3.6+**: The `triangulation` submodule path changed
2. **SciPy 1.9+**: `polyfit` and `polyval` were moved to numpy
3. **PyProj 3.0+**: Stricter parsing of projection strings

#### Platform Compatibility
- **Windows**: Fixed `strftime('%s')` which is not supported on Windows platforms
- **Cross-platform**: All fixes maintain compatibility across Linux, macOS, and Windows

### Testing
All fixes have been tested with:
- Python 3.13.3
- matplotlib 3.9.2
- scipy 1.16.0
- numpy 2.3.0
- pyproj 3.7.1

### Installation Files Added
- `setup.py`: For pip installation support
- `README.md`: Comprehensive documentation of fixes and usage
- `CHANGELOG.md`: This changelog file

## Notes
This version maintains full backward compatibility with existing PyFVCOM code while fixing critical issues that prevent the original version from working with modern Python environments.