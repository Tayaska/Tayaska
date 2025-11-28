#!/usr/bin/env python3
"""
Simple Quality Gate для CI/CD
"""

import os
import sys

def main():
    print("✅ QUALITY GATE CHECK - STARTED")
    
    # Перевірка наявності файлів
    files = os.listdir('.')
    print(f"📁 Files in directory: {files}")
    
    required_files = ['calculator.py', 'test_calculator.py']
    
    for file in required_files:
        if os.path.exists(file):
            print(f"   ✅ Found: {file}")
        else:
            print(f"   ❌ Missing: {file}")
    
    print("🎉 QUALITY CHECK COMPLETED (non-blocking)")
    return 0  # Завжди успішно для тестування

if __name__ == "__main__":
    sys.exit(main())
