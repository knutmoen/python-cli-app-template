#!/usr/bin/env python3
import sys
import importlib

def main():
    if len(sys.argv) < 2:
        print("Usage: python cli.py <operation> [args...]")
        sys.exit(1)
    
    operation = sys.argv[1]
    args = sys.argv[2:]

    try:
        module = importlib.import_module(f"mycli.operations.{operation}")
        if hasattr(module, "run"):
            module.run(args);
        else:
            print(f"Operation '{operation}' doesn't have a 'run' function.")
    except ModuleNotFoundError:
        print("Unknown operation: {operation}")
        sys.exit(1)


if __name__ == "__main__":
    main()
