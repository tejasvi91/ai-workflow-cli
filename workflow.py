from steps.data_loader import load_data
from steps.anomaly_detector import detect_anomalies
from steps.llm_step import generate_analysis
from steps.validator import validate_output
from steps.logger import save_trace


def run_workflow(file_path):

    print("📂 Loading dataset...")
    df = load_data(file_path)

    print("🔎 Detecting anomalies...")
    anomalies = detect_anomalies(df)

    print("🤖 Running AI analysis...")
    ai_output = generate_analysis(df, anomalies)

    print("✅ Validating output...")
    valid = validate_output(ai_output)

    if not valid:
        print("⚠️ AI output invalid format.")
        return

    print("📝 Saving trace...")
    save_trace(ai_output)

    print("\n🎉 Workflow Complete!\n")
    print(ai_output)