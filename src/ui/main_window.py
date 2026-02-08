import customtkinter
from search.arxiv_search import ArxivSearch
import threading
import re
from tkinter import messagebox
from utils.csv_exporter import CsvExporter
from datetime import datetime

class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("arXiv 搜尋")
        self.geometry("1100x580")

        # configure grid layout (4x4)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # create search frame
        self.search_frame = customtkinter.CTkFrame(self)
        self.search_frame.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        self.search_frame.grid_columnconfigure(0, weight=1)

        self.search_entry = customtkinter.CTkEntry(self.search_frame, placeholder_text="輸入搜尋查詢")
        self.search_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.search_entry.bind("<Return>", self.start_search_thread)
        self.search_entry.bind("<KeyRelease>", self.check_clear)

        self.author_entry = customtkinter.CTkEntry(self.search_frame, placeholder_text="作者")
        self.author_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.start_date_entry = customtkinter.CTkEntry(self.search_frame, placeholder_text="開始日期 (YYYY-MM-DD)")
        self.start_date_entry.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

        self.end_date_entry = customtkinter.CTkEntry(self.search_frame, placeholder_text="結束日期 (YYYY-MM-DD)")
        self.end_date_entry.grid(row=0, column=3, padx=10, pady=10, sticky="ew")

        self.max_results_entry = customtkinter.CTkEntry(self.search_frame, placeholder_text="最大結果數")
        self.max_results_entry.grid(row=0, column=4, padx=10, pady=10, sticky="ew")

        self.search_button = customtkinter.CTkButton(self.search_frame, text="搜尋", command=self.start_search_thread)
        self.search_button.grid(row=0, column=5, padx=10, pady=10)

        # create results textbox
        self.results_textbox = customtkinter.CTkTextbox(self, width=250)
        self.results_textbox.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

        # create export button
        self.export_button = customtkinter.CTkButton(self, text="匯出為 CSV", command=self.export_to_csv)
        self.export_button.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

        # create progressbar
        self.progressbar = customtkinter.CTkProgressBar(self, mode="indeterminate")

        # create search and export objects
        self.arxiv_search = ArxivSearch()
        self.csv_exporter = CsvExporter()
        self.current_results = []
        
        # perform initial search
        self.after(100, self.start_search_thread)


    def start_search_thread(self, event=None):
        """
        Starts a new thread to perform the search, to avoid blocking the UI.
        """
        if not self.validate_inputs():
            return
        self.progressbar.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        self.progressbar.start()
        
        search_thread = threading.Thread(target=self.perform_search)
        search_thread.start()

    def validate_inputs(self):
        """
        Validates the user inputs for date and max results.
        """
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        max_results = self.max_results_entry.get()

        date_regex = r"^\d{4}-\d{2}-\d{2}$"
        if start_date and not re.match(date_regex, start_date):
            messagebox.showerror("錯誤", "無效的開始日期格式。請使用 YYYY-MM-DD。")
            return False
        if end_date and not re.match(date_regex, end_date):
            messagebox.showerror("錯誤", "無效的結束日期格式。請使用 YYYY-MM-DD。")
            return False
        
        if max_results:
            try:
                int(max_results)
            except ValueError:
                messagebox.showerror("錯誤", "最大結果數必須是數字。")
                return False
        return True

    def perform_search(self):
        """
        Performs the search on the arXiv API.
        """
        self.results_textbox.delete("1.0", "end")
        query = self.search_entry.get()
        author = self.author_entry.get()
        start_date_str = self.start_date_entry.get()
        end_date_str = self.end_date_entry.get()
        max_results = self.max_results_entry.get()

        # Build the search query string
        search_query = []
        if query:
            search_query.append(f"all:{query}")
        if author:
            search_query.append(f"au:{author}")
        if start_date_str and end_date_str:
            # Format dates to YYYYMMDD for arXiv API
            formatted_start_date = datetime.strptime(start_date_str, "%Y-%m-%d").strftime("%Y%m%d")
            formatted_end_date = datetime.strptime(end_date_str, "%Y-%m-%d").strftime("%Y%m%d")
            search_query.append(f"submittedDate:[{formatted_start_date} TO {formatted_end_date}]")

        
        final_search_query = " AND ".join(search_query)
        if not final_search_query:
            final_search_query = "all"

        self.current_results = self.arxiv_search.search(final_search_query, max_results=int(max_results) if max_results else 10)
        
        # Update the UI from the main thread
        self.after(0, self.update_results, self.current_results)

    def update_results(self, results):
        """
        Updates the results textbox with the search results.
        """
        self.results_textbox.delete("1.0", "end")
        if not results:
            self.results_textbox.insert("end", "沒有找到結果。")
            return

        for result in results:
            self.results_textbox.insert("end", f"標題: {result.title}\n")
            self.results_textbox.insert("end", f"作者: {', '.join(author.name for author in result.authors)}\n")
            self.results_textbox.insert("end", f"發布日期: {result.published}\n")
            self.results_textbox.insert("end", f"摘要: {result.summary}\n")
            self.results_textbox.insert("end", f"網址: {result.entry_id}\n")
            self.results_textbox.insert("end", "="*20 + "\n")
        
        self.progressbar.stop()
        self.progressbar.grid_forget()

    def check_clear(self, event):
        """
        Performs a search if the search entry is cleared.
        """
        if not self.search_entry.get():
            self.start_search_thread()

    def export_to_csv(self):
        """
        Exports the current search results to a CSV file.
        """
        if self.current_results:
            self.csv_exporter.export(self.current_results)
        else:
            messagebox.showinfo("資訊", "沒有結果可匯出。")

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
