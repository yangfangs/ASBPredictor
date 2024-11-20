import os
import pandas as pd
import pickle
import argparse

class ASBPredictor:
    def __init__(self, model_path=None):
        # 默认加载模型文件
        self.model_path = model_path or os.path.join(os.path.dirname(__file__), 'model.pkl')
        self._load_model()

    def _load_model(self):
        # 从文件加载模型
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Model file not found: {self.model_path}")
        with open(self.model_path, 'rb') as f:
            self.model = pickle.load(f)

    def predict(self, input_csv_path, output_csv_path):
        # 读取输入 CSV 文件
        if not os.path.exists(input_csv_path):
            raise FileNotFoundError(f"Input file not found: {input_csv_path}")
        df = pd.read_csv(input_csv_path)

        # 确保输入的列符合预期
        expected_columns = ["CXM", "CRP", "Na", "BACT", "WBC", "WBCC", "MONV",
                            "CRO", "GGT", "ALT", "GLU.1", "FOX", "AST", "RDWCV",
                            "Urea", "Cl", "WBCHP", "TP", "GLO", "FOB"]
        missing_columns = [col for col in expected_columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Missing columns in input file: {missing_columns}")

        # 预测并添加 "ASB Risk" 列
        predictions = self.model.predict_proba(df[expected_columns])[:, 1]
        df["ASB Risk"] = predictions

        # 保存结果到输出文件
        df.to_csv(output_csv_path, index=False)
        print(f"Results saved to {output_csv_path}")
        return output_csv_path


def main():
    parser = argparse.ArgumentParser(description="ASBPredictor: Predict ASB Risk from clinical data")
    parser.add_argument("-i", "--input", required=True, help="Path to input CSV file")
    parser.add_argument("-o", "--output", required=True, help="Path to output CSV file")

    args = parser.parse_args()

    predictor = ASBPredictor()
    predictor.predict(args.input, args.output)


if __name__ == "__main__":
    main()
