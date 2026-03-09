# 基於深度學習之中文醫療問答系統
### (Medical Question Answering System based on Deep Learning)

本專案為輔仁大學電機工程學系大學部畢業專案。實現了一個結合 **RNN (LSTM)** 與 **CNN** 並導入 **注意力機制 (Attention Mechanism)** 的中文醫療問答框架。

## 🌟 技術亮點
- **架構設計**：採用 ABCNN (Attention-Based CNN) 結構，有效捕捉問題與答案間的語意關聯。
- **NLP 實作**：
  - 建置醫療領域專用詞庫，解決專有名詞識別挑戰。
  - 應用 Word/Character Embedding 技術進行文本向量化。
- **實驗成果**：在 cMedQA 資料集上達到 **84.83%** 的測試準確率。

## 📂 專案成果文件
- [專案簡報 (Presentation PDF)](docs/Project_Presentation.pdf)
- [技術海報 (Poster PDF)](docs/Project_Poster.pdf)

## 📊 數據處理範例 (Python)
以下為使用 Python 進行醫療語料預處理與基礎分析的示範程式碼：

```python
import pandas as pd

def analyze_medical_data(file_path):
    """
    讀取並分析醫療問答數據的基礎統計
    """
    print(f"正在分析醫療問答數據：{file_path}")
    
    # 讀取資料
    df = pd.read_csv(file_path)
    
    # 顯示前五筆資料，證明讀取成功
    print("\n--- 數據預覽 ---")
    print(df.head())
    
    # 基礎統計：計算問題的平均長度
    if 'question' in df.columns:
        avg_len = df['question'].str.len().mean()
        print(f"\n平均問題長度: {avg_len:.2f} 字")

if __name__ == "__main__":
    # 執行分析 (假設數據已存放於 data/sample.csv)
    # analyze_medical_data('data/sample.csv')
    pass
