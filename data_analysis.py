import pandas as pd
import os

def run_medical_data_analysis(file_path):
    """
    執行醫療問答數據的基礎統計分析
    """
    if not os.path.exists(file_path):
        print(f"錯誤：找不到檔案 {file_path}")
        return

    print(f"--- 開始分析醫療數據：{file_path} ---")
    
    # 讀取資料
    df = pd.read_csv(file_path)
    
    # 1. 顯示基本資訊
    print("\n[數據概況]")
    print(df.info())
    
    # 2. 顯示前幾筆資料
    print("\n[前 5 筆數據預覽]")
    print(df.head())
    
    # 3. 基礎統計 (假設欄位名為 question)
    # 這裡可以根據你 sample.csv 的實際欄位名稱調整
    target_col = 'question' if 'question' in df.columns else df.columns[0]
    
    print(f"\n[針對 {target_col} 欄位的統計]")
    avg_len = df[target_col].astype(str).str.len().mean()
    print(f"平均文本長度: {avg_len:.2f} 字")
    print(f"總筆數: {len(df)} 筆")

if __name__ == "__main__":
    # 指向你上傳的 sample.csv 路徑
    data_path = 'data/sample.csv'
    run_medical_data_analysis(data_path)
