<!--
Sync Impact Report:
- Version change: 1.0.0 → 2.0.0
- List of modified principles: Complete overhaul, principles replaced.
- Added sections: 核心開發準則, 程式碼風格與結構, 領域特定邏輯 (Domain Specific), 環境安全與整合
- Removed sections: Core Principles, SECTION_2_NAME, SECTION_3_NAME, Governance
- Templates requiring updates:
  - ⚠ pending: .specify/templates/plan-template.md
  - ⚠ pending: .specify/templates/spec-template.md
  - ⚠ pending: .specify/templates/tasks-template.md
- Follow-up TODOs:
  - TODO(RATIFICATION_DATE): Determine the original ratification date.
-->
# 專案憲法 (Project Constitution) - arXiv Research Assistant

## 1. 核心開發準則
* **Python 版本限制**：必須相容於 Python 3.12。嚴格禁止使用僅在 Python 3.14+ 提供的特性，以確保開發環境穩定。
* **依賴管理**：優先使用 `pip` 或 `uv` 進行套件管理。所有新增的依賴必須記錄在 `requirements.txt` 中。
* **錯誤處理**：所有 API 呼叫（如 arxiv client）必須包含 `try-except` 區塊，並針對網路錯誤與無結果情況提供友善的提示。

## 2. 程式碼風格與結構
* **語言與註解**：程式碼實作（變數、函數名）使用英文，但功能說明、Docstrings 以及 Print 輸出訊息必須使用 **正體中文**。
* **模組化設計**：邏輯需與介面分離。搜尋邏輯應封裝在類別（Class）中，而非散落在全域空間。
* **非同步支援**：考量到未來可能增加大量搜尋，建議評估使用 `asyncio` 來提升 I/O 效率。

## 3. 領域特定邏輯 (Domain Specific)
* **自動分類建議**：由於使用者頻繁搜尋分子生物學（q-bio）與化妝品科學相關內容，系統應預設提供相關領域的分類過濾（如 `cat:q-bio.*`）。
* **格式化輸出**：搜尋結果除了列印在終端機，必須支援匯出為 Markdown 格式，以便紀錄於研究日誌。

## 4. 環境安全與整合
* **Git 規範**：所有 Commit Message 必須清晰且包含功能描述。
* **虛擬環境保護**：禁止程式自動修改 `.venv` 以外的系統環境變數。

**Version**: 2.0.0 | **Ratified**: TODO(RATIFICATION_DATE) | **Last Amended**: 2026-02-08