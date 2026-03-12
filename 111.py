# %%
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

# 1. 윈도우 한글 폰트 설정 (맑은 고딕)
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지

# 2. 데이터 로드 (경로는 사용자님의 PC 환경에 맞게 수정하세요)
csv_path = r'.\for_link.csv' 
# 만약 위 경로가 없다면 현재 폴더의 파일을 읽도록 예외 처리
if not os.path.exists(csv_path):
    csv_path = r'.\for_link.csv'

try:
    df = pd.read_csv(csv_path)
    print("✅ 데이터를 성공적으로 불러왔습니다.")
except Exception as e:
    print(f"❌ 파일 읽기 오류: {e}")
    # 테스트용 데이터셋 생성 (파일이 없을 경우 대비)
    df = pd.DataFrame({
        '연도': [2022, 2022, 2023, 2023, 2024],
        '성별': ['남자', '여자', '남자', '여자', '여자'],
        '인원(명)': [100, 120, 110, 130, 150],
        '자치구명': ['종로구', '종로구', '강남구', '강남구', '종로구']
    })

# %%
def custom_visualizer(input_df):
    """사용자 입력을 받아 그래프를 그리는 함수"""
    df_temp = input_df.copy()
    
    # 성별 컬럼 공백 제거 전처리
    if '성별' in df_temp.columns:
        df_temp['성별'] = df_temp['성별'].str.strip()

    print("\n" + "="*30)
    print("📊 분석 가능한 컬럼 목록:")
    print(list(df_temp.columns))
    print("="*30)

    # VS Code 터미널에서 입력 받기
    try:
        x_axis = input("1. X축으로 쓸 컬럼명 입력 (예: 연도, 자치구명): ").strip()
        y_value = input("2. 합계를 구할 컬럼명 입력 (예: 인원(명)): ").strip()
        chart_kind = input("3. 그래프 종류 입력 (bar, line, pie): ").strip()

        # 데이터 집계
        analysis_result = df_temp.groupby(x_axis)[y_value].sum()

        # 그래프 그리기
        plt.figure(figsize=(10, 6))
        
        if chart_kind == 'pie':
            analysis_result.plot(kind=chart_kind, autopct='%1.1f%%', startangle=90, cmap='Set3')
            plt.ylabel("")
        else:
            # 기본 색상 설정 및 마커 추가
            analysis_result.plot(kind=chart_kind, color='#3498db', marker='o' if chart_kind=='line' else None)
            plt.grid(True, axis='y', linestyle='--', alpha=0.5)
            plt.ylabel(y_value)

        plt.title(f"<{x_axis}> 기준 <{y_value}> 합계 추이 ({chart_kind})", fontsize=14, pad=15)
        plt.xlabel(x_axis)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        print("\n📈 그래프 창이 팝업되었습니다. 확인해 보세요!")
        plt.show() # VS Code에서는 새 창으로 그래프가 뜹니다.
        
        return analysis_result

    except KeyError as e:
        print(f"\n❌ 오류: 컬럼명을 잘못 입력하셨습니다. ({e})")
    except Exception as e:
        print(f"\n❌ 예기치 못한 오류 발생: {e}")
# %%
# --- 실행부 ---
if __name__ == "__main__":
    result = custom_visualizer(df)
    if result is not None:
        print("\n[집계된 데이터 요약]")
        print(result)