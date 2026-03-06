import argparse
from workflow import run_workflow

def main():
    parser = argparse.ArgumentParser(description="AI Workflow Engine CLI")

    subparsers = parser.add_subparsers(dest="command")

    run_parser = subparsers.add_parser("run")
    run_parser.add_argument("file", help="Path to CSV file")

    args = parser.parse_args()

    if args.command == "run":
        print("\n🚀 Running AI Workflow Engine...\n")
        run_workflow(args.file)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()