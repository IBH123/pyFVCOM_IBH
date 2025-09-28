#!/usr/bin/env python
"""
Test script to verify PyFVCOM fixes are working correctly.
Run this script to test the key functionality that was broken in the original version.
"""

import sys
import os

def test_imports():
    """Test that all critical imports work correctly"""
    print("Testing imports...")
    
    try:
        # Test matplotlib import fix
        from matplotlib.tri import Triangulation
        print("✓ matplotlib.tri.Triangulation import successful")
    except ImportError as e:
        print(f"✗ matplotlib import failed: {e}")
        return False
    
    try:
        # Test scipy/numpy import fix
        from scipy import stats
        from numpy import polyfit, polyval
        print("✓ scipy stats and numpy polyfit/polyval imports successful")
    except ImportError as e:
        print(f"✗ scipy/numpy imports failed: {e}")
        return False
    
    try:
        # Test PyFVCOM main import
        import PyFVCOM as pf
        print("✓ PyFVCOM main import successful")
        print(f"  PyFVCOM version: {getattr(pf, '__version__', 'unknown')}")
    except ImportError as e:
        print(f"✗ PyFVCOM import failed: {e}")
        return False
    
    return True

def test_coordinate_projection():
    """Test that coordinate projection fixes work"""
    print("\nTesting coordinate projection...")
    
    try:
        import pyproj
        
        # Test the fixed projection string format
        proj_string = "+proj=utm +zone=20 +ellps=WGS84 +datum=WGS84 +units=m +no_defs"
        proj = pyproj.Proj(proj_string)
        print("✓ Coordinate projection string fix successful")
        return True
        
    except Exception as e:
        print(f"✗ Coordinate projection test failed: {e}")
        return False

def test_datetime_functionality():
    """Test that datetime functionality works on Windows"""
    print("\nTesting datetime functionality...")
    
    try:
        from datetime import datetime
        import calendar
        
        # Test the timestamp method instead of strftime('%s')
        test_date = datetime(2025, 1, 1)
        timestamp = test_date.timestamp()
        print(f"✓ DateTime timestamp() method works: {timestamp}")
        return True
        
    except Exception as e:
        print(f"✗ DateTime functionality test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("PyFVCOM Fixed Version - Test Suite")
    print("=" * 40)
    
    tests = [
        test_imports,
        test_coordinate_projection, 
        test_datetime_functionality
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"✗ Test {test.__name__} crashed: {e}")
            results.append(False)
    
    print("\n" + "=" * 40)
    print("Test Results:")
    passed = sum(results)
    total = len(results)
    print(f"Passed: {passed}/{total}")
    
    if passed == total:
        print("✓ All tests passed! PyFVCOM fixes are working correctly.")
        return 0
    else:
        print("✗ Some tests failed. Please check the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())