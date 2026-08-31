import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from cryptography.fernet import Fernet
import threading


LANG = {
    "ar": {
        "title": "LockTab - \u0623\u062f\u0627\u0629 \u062a\u0634\u0641\u064a\u0631 \u0627\u0644\u0645\u0644\u0641\u0627\u062a",
        "lang_btn": "English",
        "title_bar": "\u0644\u0648\u0643\u0637\u0627\u0628 - \u0623\u062f\u0627\u0629 \u062a\u0634\u0641\u064a\u0631 \u0627\u0644\u0645\u0644\u0641\u0627\u062a",
        "key_frame": "\u0627\u0644\u0645\u0641\u062a\u0627\u062d",
        "gen_key": "\u062a\u0648\u0644\u064a\u062f \u0645\u0641\u062a\u0627\u062d \u062c\u062f\u064a\u062f",
        "copy_key": "\u0646\u0633\u062e \u0627\u0644\u0645\u0641\u062a\u0627\u062d",
        "paste_key": "\u0644\u0635\u0642 \u0627\u0644\u0645\u0641\u062a\u0627\u062d",
        "key_placeholder": "\u0623\u062f\u062e\u0644 \u0627\u0644\u0645\u0641\u062a\u0627\u062d \u0647\u0646\u0627 \u0623\u0648 \u0642\u0645 \u0628\u062a\u0648\u0644\u064a\u062f\u0647 \u0623\u0648\u0644\u0627\u064b...",
        "folder_frame": "\u0627\u0644\u0645\u062c\u0644\u062f",
        "choose_folder": "\u0627\u062e\u062a\u0631 \u0627\u0644\u0645\u062c\u0644\u062f...",
        "no_folder": "\u0644\u0645 \u064a\u062a\u0645 \u0627\u062e\u062a\u064a\u0627\u0631 \u0645\u062c\u0644\u062f",
        "enc_btn": "\u062a\u0634\u0641\u064a\u0631 \u0627\u0644\u0645\u062c\u0644\u062f \u0628\u0627\u0644\u0643\u0627\u0645\u0644",
        "dec_btn": "\u0641\u0643 \u062a\u0634\u0641\u064a\u0631 \u0627\u0644\u0645\u062c\u0644\u062f",
        "status": "\u0627\u0644\u062d\u0627\u0644\u0629",
        "ready": "\u062c\u0627\u0647\u0632",
        "generating": "\u062c\u0627\u0631\u064a \u062a\u0648\u0644\u064a\u062f \u0627\u0644\u0645\u0641\u062a\u0627\u062d...",
        "key_generated": "\u062a\u0645 \u062a\u0648\u0644\u064a\u062f \u0627\u0644\u0645\u0641\u062a\u0627\u062d \u0628\u0646\u062c\u0627\u062d! \u0627\u0646\u0633\u062e\u0647 \u0648\u0627\u062d\u0641\u0638\u0647 \u0641\u064a \u0645\u0643\u0627\u0646 \u0622\u0645\u0646.",
        "key_copied": "\u062a\u0645 \u0646\u0633\u062e \u0627\u0644\u0645\u0641\u062a\u0627\u062d \u0625\u0644\u0649 \u0627\u0644\u062d\u0627\u0636\u0639\u0629.",
        "key_pasted": "\u062a\u0645 \u0644\u0635\u0642 \u0627\u0644\u0645\u0641\u062a\u0627\u062d \u0645\u0646 \u0627\u0644\u062d\u0627\u0636\u0639\u0629.",
        "folder_selected": "\u0645\u062c\u0644\u062f \u0645\u062d\u062f\u062f: {0}",
        "select_folder": "\u064a\u0631\u062c\u0649 \u0627\u062e\u062a\u064a\u0627\u0631 \u0645\u062c\u0644\u062f \u0623\u0648\u0644\u0627\u064b.",
        "enter_key": "\u064a\u0631\u062c\u0649 \u0625\u062f\u062e\u0627\u0644 \u0627\u0644\u0645\u0641\u062a\u0627\u062d \u0623\u0648\u0644\u0627\u064b.",
        "confirm_enc": "\u0647\u0644 \u0623\u0646\u062a \u0645\u062a\u0623\u0643\u062f \u0645\u0646 \u062a\u0634\u0641\u064a\u0631 \u0647\u0630\u0627 \u0627\u0644\u0645\u062c\u0644\u062f\u061f\n\n{0}\n\n\u062a\u062d\u0630\u064a\u0631: \u0627\u062d\u0641\u0638 \u0627\u0644\u0645\u0641\u062a\u0627\u062d \u0641\u064a \u0645\u0643\u0627\u0646 \u0622\u0645\u0646 \u0642\u0628\u0644 \u0627\u0644\u0645\u062a\u0627\u0628\u0639\u0629!",
        "confirm_dec": "\u0647\u0644 \u0623\u0646\u062a \u0645\u062a\u0623\u0643\u062f \u0645\u0646 \u0641\u0643 \u062a\u0634\u0641\u064a\u0631 \u0647\u0630\u0627 \u0627\u0644\u0645\u062c\u0644\u062f\u061f\n\n{0}",
        "processing": "\u062c\u0627\u0631\u064a \u0627\u0644\u0645\u0639\u0627\u0644\u062c\u0629... ({0}/{1})",
        "enc_done": "\u062a\u0645 \u0627\u0644\u062a\u0634\u0641\u064a\u0631 \u0628\u0646\u062c\u0627\u062d!\n\n\u0639\u062f\u062f \u0627\u0644\u0645\u0644\u0641\u0627\u062a: {0}",
        "dec_done": "\u062a\u0645 \u0641\u0643 \u0627\u0644\u062a\u0634\u0641\u064a\u0631 \u0628\u0646\u062c\u0627\u062d!\n\n\u0639\u062f\u062f \u0627\u0644\u0645\u0644\u0641\u0627\u062a: {0}",
        "error": "\u062e\u0637\u0623",
        "enc_error": "\u062d\u062f\u062b \u062e\u0637\u0623 \u0623\u062b\u0646\u0627\u0621 \u0627\u0644\u062a\u0634\u0641\u064a\u0631:\n{0}",
        "dec_error": "\u062d\u062f\u062b \u062e\u0637\u0623 \u0623\u062b\u0646\u0627\u0621 \u0641\u0643 \u0627\u0644\u062a\u0634\u0641\u064a\u0631:\n{0}",
        "key_error": "\u0627\u0644\u0645\u0641\u062a\u0627\u062d \u063a\u064a\u0631 \u0635\u062d\u064a\u062d! \u0644\u0627 \u064a\u0645\u0643\u0646 \u0641\u0643 \u0627\u0644\u062a\u0634\u0641\u064a\u0631.",
        "cancelled": "\u062a\u0645 \u0627\u0644\u0625\u0644\u063a\u0627\u0621.",
        "about": "\u062d\u0648\u0644",
        "about_msg": "LockTab - \u0623\u062f\u0627\u0629 \u062a\u0634\u0641\u064a\u0631 \u0627\u0644\u0645\u0644\u0641\u0627\u062a\n\n\u062a\u0634\u0641\u064a\u0631 AES-256 \u0628\u0627\u0633\u062a\u062e\u062f\u0627\u0645 Fernet\n\nPowered by the L house",
        "footer": "Powered by the L house",
        "file_types": ["\u0627\u0644\u0643\u0644"],
    },
    "en": {
        "title": "LockTab - File Encryption Tool",
        "lang_btn": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
        "title_bar": "LockTab - File Encryption Tool",
        "key_frame": "Key",
        "gen_key": "Generate New Key",
        "copy_key": "Copy Key",
        "paste_key": "Paste Key",
        "key_placeholder": "Enter key here or generate one first...",
        "folder_frame": "Folder",
        "choose_folder": "Choose Folder...",
        "no_folder": "No folder selected",
        "enc_btn": "Encrypt Entire Folder",
        "dec_btn": "Decrypt Folder",
        "status": "Status",
        "ready": "Ready",
        "generating": "Generating key...",
        "key_generated": "Key generated successfully! Copy and save it somewhere safe.",
        "key_copied": "Key copied to clipboard.",
        "key_pasted": "Key pasted from clipboard.",
        "folder_selected": "Selected: {0}",
        "select_folder": "Please select a folder first.",
        "enter_key": "Please enter a key first.",
        "confirm_enc": "Are you sure you want to encrypt this folder?\n\n{0}\n\nWarning: Save the key somewhere safe before proceeding!",
        "confirm_dec": "Are you sure you want to decrypt this folder?\n\n{0}",
        "processing": "Processing... ({0}/{1})",
        "enc_done": "Encryption completed!\n\nFiles processed: {0}",
        "dec_done": "Decryption completed!\n\nFiles processed: {0}",
        "error": "Error",
        "enc_error": "An error occurred during encryption:\n{0}",
        "dec_error": "An error occurred during decryption:\n{0}",
        "key_error": "Invalid key! Decryption failed.",
        "cancelled": "Cancelled.",
        "about": "About",
        "about_msg": "LockTab - File Encryption Tool\n\nAES-256 encryption using Fernet\n\nPowered by the L house",
        "footer": "Powered by the L house",
        "file_types": ["All"],
    },
}


class Win95Style:
    BG = "#c0c0c0"
    FG = "#000000"
    BTN_BG = "#c0c0c0"
    BTN_FG = "#000000"
    ENTRY_BG = "#ffffff"
    ENTRY_FG = "#000000"
    FRAME_BG = "#c0c0c0"
    LABEL_BG = "#c0c0c0"
    TITLE_BG = "#000080"
    TITLE_FG = "#ffffff"
    BORDER_LIGHT = "#ffffff"
    BORDER_DARK = "#808080"
    BORDER_DARKEST = "#404040"
    FOOTER_BG = "#808080"
    FOOTER_FG = "#c0c0c0"


class LockTabApp:
    def __init__(self, root):
        self.root = root
        self.lang = "ar"
        self.selected_folder = None
        self.running = False
        self._build_ui()
        self._apply_lang()

    def _build_ui(self):
        self.root.title(LANG[self.lang]["title"])
        self.root.configure(bg=Win95Style.BG)
        self.root.minsize(540, 520)
        self.root.resizable(True, True)

        self._set_icon()

        menubar = tk.Menu(self.root, bg=Win95Style.BG, fg=Win95Style.FG,
                          activebackground=Win95Style.TITLE_BG,
                          activeforeground=Win95Style.TITLE_FG)
        help_menu = tk.Menu(menubar, tearoff=0, bg=Win95Style.BG, fg=Win95Style.FG)
        help_menu.add_command(label="", command=self._show_about)
        menubar.add_cascade(label="", menu=help_menu)
        self.root.config(menu=menubar)
        self._menubar = menubar
        self._help_menu = help_menu

        main_frame = tk.Frame(self.root, bg=Win95Style.BG, bd=0)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=6, pady=6)

        self._build_title_bar(main_frame)
        self._build_key_frame(main_frame)
        self._build_folder_frame(main_frame)
        self._build_action_frame(main_frame)
        self._build_progress_frame(main_frame)
        self._build_footer(self.root)

    def _set_icon(self):
        try:
            if getattr(sys, 'frozen', False):
                base = sys._MEIPASS
            else:
                base = os.path.dirname(os.path.abspath(__file__))
            icon_path = os.path.join(base, "icon.ico")
            if os.path.exists(icon_path):
                self.root.iconbitmap(icon_path)
        except Exception:
            pass

    def _build_title_bar(self, parent):
        bar = tk.Frame(parent, bg=Win95Style.TITLE_BG, height=36, bd=0)
        bar.pack(fill=tk.X, pady=(0, 6))
        bar.pack_propagate(False)

        inner = tk.Frame(bar, bg=Win95Style.TITLE_BG)
        inner.pack(fill=tk.BOTH, expand=True, padx=4, pady=2)

        self._title_label = tk.Label(inner, bg=Win95Style.TITLE_BG,
                                     fg=Win95Style.TITLE_FG,
                                     font=("MS Sans Serif", 12, "bold"),
                                     anchor="center")
        self._title_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.lang_btn = tk.Button(inner, command=self._toggle_lang,
                                  relief=tk.RAISED, bd=2,
                                  bg=Win95Style.BTN_BG, fg=Win95Style.BTN_FG,
                                  activebackground=Win95Style.TITLE_BG,
                                  activeforeground=Win95Style.TITLE_FG,
                                  font=("MS Sans Serif", 9, "bold"),
                                  padx=10, pady=2)
        self.lang_btn.pack(side=tk.RIGHT, padx=(4, 0))

    def _build_key_frame(self, parent):
        frame = tk.LabelFrame(parent, bg=Win95Style.FRAME_BG, fg=Win95Style.FG,
                              bd=2, relief=tk.RIDGE, padx=8, pady=8)
        frame.pack(fill=tk.X, pady=(0, 4))

        self._key_frame_label = tk.Label(frame, bg=Win95Style.FRAME_BG,
                                         fg=Win95Style.FG, anchor="w",
                                         font=("MS Sans Serif", 9, "bold"))
        self._key_frame_label.pack(fill=tk.X)

        key_row = tk.Frame(frame, bg=Win95Style.FRAME_BG)
        key_row.pack(fill=tk.X, pady=(4, 0))

        self.key_var = tk.StringVar()
        self.key_entry = tk.Entry(key_row, textvariable=self.key_var,
                                  bg=Win95Style.ENTRY_BG, fg=Win95Style.ENTRY_FG,
                                  insertbackground=Win95Style.ENTRY_FG,
                                  relief=tk.SUNKEN, bd=2,
                                  font=("Courier New", 9))
        self.key_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 4))

        btn_row = tk.Frame(frame, bg=Win95Style.FRAME_BG)
        btn_row.pack(fill=tk.X, pady=(6, 0))

        self.gen_key_btn = tk.Button(btn_row, command=self._generate_key,
                                     relief=tk.RAISED, bd=2,
                                     bg=Win95Style.BTN_BG, fg=Win95Style.BTN_FG,
                                     activebackground=Win95Style.TITLE_BG,
                                     activeforeground=Win95Style.TITLE_FG,
                                     font=("MS Sans Serif", 9, "bold"))
        self.gen_key_btn.pack(side=tk.LEFT, padx=(0, 4))

        self.copy_key_btn = tk.Button(btn_row, command=self._copy_key,
                                      relief=tk.RAISED, bd=2,
                                      bg=Win95Style.BTN_BG, fg=Win95Style.BTN_FG,
                                      font=("MS Sans Serif", 9))
        self.copy_key_btn.pack(side=tk.LEFT, padx=(0, 4))

        self.paste_key_btn = tk.Button(btn_row, command=self._paste_key,
                                       relief=tk.RAISED, bd=2,
                                       bg=Win95Style.BTN_BG, fg=Win95Style.BTN_FG,
                                       font=("MS Sans Serif", 9))
        self.paste_key_btn.pack(side=tk.LEFT)

    def _build_folder_frame(self, parent):
        frame = tk.LabelFrame(parent, bg=Win95Style.FRAME_BG, fg=Win95Style.FG,
                              bd=2, relief=tk.RIDGE, padx=8, pady=8)
        frame.pack(fill=tk.X, pady=(0, 4))

        self._folder_frame_label = tk.Label(frame, bg=Win95Style.FRAME_BG,
                                            fg=Win95Style.FG, anchor="w",
                                            font=("MS Sans Serif", 9, "bold"))
        self._folder_frame_label.pack(fill=tk.X)

        folder_row = tk.Frame(frame, bg=Win95Style.FRAME_BG)
        folder_row.pack(fill=tk.X, pady=(4, 0))

        self.choose_btn = tk.Button(folder_row, command=self._choose_folder,
                                    relief=tk.RAISED, bd=2,
                                    bg=Win95Style.BTN_BG, fg=Win95Style.BTN_FG,
                                    font=("MS Sans Serif", 9))
        self.choose_btn.pack(side=tk.LEFT, padx=(0, 8))

        self.folder_label = tk.Label(folder_row, bg=Win95Style.ENTRY_BG,
                                     fg=Win95Style.FG, anchor="w",
                                     relief=tk.SUNKEN, bd=2, padx=4, pady=2,
                                     font=("MS Sans Serif", 9))
        self.folder_label.pack(side=tk.LEFT, fill=tk.X, expand=True)

    def _build_action_frame(self, parent):
        frame = tk.Frame(parent, bg=Win95Style.BG)
        frame.pack(fill=tk.X, pady=(8, 4))

        self.enc_btn = tk.Button(frame, command=self._encrypt_folder,
                                 relief=tk.RAISED, bd=3,
                                 bg="#d4a0a0", fg="#800000",
                                 activebackground="#b08080",
                                 font=("MS Sans Serif", 10, "bold"),
                                 padx=12, pady=6)
        self.enc_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 4))

        self.dec_btn = tk.Button(frame, command=self._decrypt_folder,
                                 relief=tk.RAISED, bd=3,
                                 bg="#a0d4a0", fg="#006000",
                                 activebackground="#80b080",
                                 font=("MS Sans Serif", 10, "bold"),
                                 padx=12, pady=6)
        self.dec_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(4, 0))

    def _build_progress_frame(self, parent):
        frame = tk.LabelFrame(parent, bg=Win95Style.FRAME_BG, fg=Win95Style.FG,
                              bd=2, relief=tk.RIDGE, padx=8, pady=8)
        frame.pack(fill=tk.X, pady=(0, 4))

        self._status_frame_label = tk.Label(frame, bg=Win95Style.FRAME_BG,
                                            fg=Win95Style.FG, anchor="w",
                                            font=("MS Sans Serif", 9, "bold"))
        self._status_frame_label.pack(fill=tk.X)

        self.progress_var = tk.DoubleVar(value=0)
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Win95.Horizontal.TProgressbar",
                        background="#000080",
                        troughcolor="#c0c0c0",
                        borderwidth=2,
                        lightcolor="#ffffff",
                        darkcolor="#808080")

        self.progress_bar = ttk.Progressbar(frame, variable=self.progress_var,
                                            maximum=100,
                                            style="Win95.Horizontal.TProgressbar",
                                            length=300)
        self.progress_bar.pack(fill=tk.X, pady=(4, 4))

        self.status_label = tk.Label(frame, bg=Win95Style.FRAME_BG,
                                     fg=Win95Style.FG, anchor="w",
                                     font=("MS Sans Serif", 9))
        self.status_label.pack(fill=tk.X)

    def _build_footer(self, parent):
        sep = tk.Frame(parent, bg=Win95Style.BORDER_DARK, height=2)
        sep.pack(fill=tk.X, side=tk.BOTTOM)

        footer = tk.Frame(parent, bg=Win95Style.FOOTER_BG, bd=0, height=30)
        footer.pack(fill=tk.X, side=tk.BOTTOM)
        footer.pack_propagate(False)

        inner = tk.Frame(footer, bg=Win95Style.FOOTER_BG)
        inner.pack(fill=tk.BOTH, expand=True)

        self.footer_label = tk.Label(inner, bg=Win95Style.FOOTER_BG,
                                     fg=Win95Style.FOOTER_FG,
                                     font=("MS Sans Serif", 8, "bold"),
                                     anchor="center")
        self.footer_label.pack(fill=tk.BOTH, expand=True)

    def _apply_lang(self):
        t = LANG[self.lang]
        self.root.title(t["title"])

        self._title_label.config(text=t["title_bar"])
        self.lang_btn.config(text=t["lang_btn"])

        self._key_frame_label.config(text=t["key_frame"])
        self.gen_key_btn.config(text=t["gen_key"])
        self.copy_key_btn.config(text=t["copy_key"])
        self.paste_key_btn.config(text=t["paste_key"])

        if not self.key_var.get() or self.key_var.get() in [LANG["ar"]["key_placeholder"], LANG["en"]["key_placeholder"]]:
            self.key_var.set("")
            self.key_entry.config(fg=Win95Style.ENTRY_FG)
            self.key_entry.delete(0, tk.END)
            self.key_entry.insert(0, t["key_placeholder"])
            self.key_entry.config(fg="#808080")
            self.key_entry.bind("<FocusIn>", self._on_key_focus_in)
            self.key_entry.bind("<FocusOut>", self._on_key_focus_out)

        self._folder_frame_label.config(text=t["folder_frame"])
        self.choose_btn.config(text=t["choose_folder"])
        if not self.selected_folder:
            self.folder_label.config(text=t["no_folder"])

        self.enc_btn.config(text=t["enc_btn"])
        self.dec_btn.config(text=t["dec_btn"])

        self._status_frame_label.config(text=t["status"])
        if not self.running:
            self.status_label.config(text=t["ready"])

        self.footer_label.config(text=t["footer"])

        self._menubar.delete(0, "end")
        self._menubar.add_cascade(label=t["about"], menu=self._help_menu)

        self._help_menu.delete(0, "end")
        self._help_menu.add_command(label=t["about"], command=self._show_about)

    def _on_key_focus_in(self, event=None):
        t = LANG[self.lang]
        if self.key_var.get() == t["key_placeholder"]:
            self.key_var.set("")
            self.key_entry.config(fg=Win95Style.ENTRY_FG)

    def _on_key_focus_out(self, event=None):
        t = LANG[self.lang]
        if not self.key_var.get():
            self.key_var.set(t["key_placeholder"])
            self.key_entry.config(fg="#808080")

    def _toggle_lang(self):
        self.lang = "en" if self.lang == "ar" else "ar"
        self._apply_lang()

    def _show_about(self):
        messagebox.showinfo(LANG[self.lang]["about"], LANG[self.lang]["about_msg"])

    def _generate_key(self):
        self.status_label.config(text=LANG[self.lang]["generating"])
        self.root.update()

        def do_gen():
            key = Fernet.generate_key().decode()
            self.root.after(0, lambda: self._set_key(key))

        threading.Thread(target=do_gen, daemon=True).start()

    def _set_key(self, key):
        self.key_var.set(key)
        self.key_entry.config(fg=Win95Style.ENTRY_FG)
        self.status_label.config(text=LANG[self.lang]["ready"])
        messagebox.showinfo(LANG[self.lang]["status"], LANG[self.lang]["key_generated"])

    def _copy_key(self):
        key = self.key_var.get()
        t = LANG[self.lang]
        if not key or key == t["key_placeholder"]:
            return
        self.root.clipboard_clear()
        self.root.clipboard_append(key)
        self.status_label.config(text=t["key_copied"])

    def _paste_key(self):
        try:
            clip = self.root.clipboard_get()
            self.key_var.set(clip)
            self.key_entry.config(fg=Win95Style.ENTRY_FG)
            self.status_label.config(text=LANG[self.lang]["key_pasted"])
        except tk.TclError:
            pass

    def _choose_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.selected_folder = folder
            display = folder if len(folder) <= 50 else "..." + folder[-47:]
            self.folder_label.config(text=LANG[self.lang]["folder_selected"].format(display))

    def _validate_before_action(self):
        t = LANG[self.lang]
        if not self.selected_folder:
            messagebox.showwarning(t["error"], t["select_folder"])
            return False
        key = self.key_var.get()
        if not key or key == t["key_placeholder"]:
            messagebox.showwarning(t["error"], t["enter_key"])
            return False
        if self.running:
            return False
        return True

    def _set_running(self, val):
        self.running = val
        state = tk.DISABLED if val else tk.NORMAL
        self.enc_btn.config(state=state)
        self.dec_btn.config(state=state)
        self.gen_key_btn.config(state=state)
        self.choose_btn.config(state=state)

    def _encrypt_folder(self):
        if not self._validate_before_action():
            return
        t = LANG[self.lang]
        if not messagebox.askyesno(t["enc_btn"], t["confirm_enc"].format(self.selected_folder)):
            return
        self._set_running(True)
        threading.Thread(target=self._do_encrypt, daemon=True).start()

    def _decrypt_folder(self):
        if not self._validate_before_action():
            return
        t = LANG[self.lang]
        if not messagebox.askyesno(t["dec_btn"], t["confirm_dec"].format(self.selected_folder)):
            return
        self._set_running(True)
        threading.Thread(target=self._do_decrypt, daemon=True).start()

    def _collect_files(self, folder):
        files = []
        for root_dir, dirs, filenames in os.walk(folder):
            for fname in filenames:
                fpath = os.path.join(root_dir, fname)
                if os.path.isfile(fpath):
                    files.append(fpath)
        return files

    def _update_progress(self, current, total):
        pct = (current / total) * 100 if total > 0 else 0
        self.root.after(0, lambda: self.progress_var.set(pct))
        self.root.after(0, lambda: self.status_label.config(
            text=LANG[self.lang]["processing"].format(current, total)))

    def _do_encrypt(self):
        t = LANG[self.lang]
        try:
            key = self.key_var.get().strip().encode()
            fernet = Fernet(key)
            files = self._collect_files(self.selected_folder)
            total = len(files)
            count = 0

            for i, fpath in enumerate(files):
                self._update_progress(i, total)
                try:
                    with open(fpath, "rb") as f:
                        data = f.read()
                    encrypted = fernet.encrypt(data)
                    with open(fpath, "wb") as f:
                        f.write(encrypted)
                    count += 1
                except Exception:
                    continue

            self._update_progress(total, total)
            self.root.after(0, lambda: messagebox.showinfo(
                t["enc_btn"], t["enc_done"].format(count)))
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror(
                t["error"], t["enc_error"].format(str(e))))
        finally:
            self.root.after(0, lambda: self._set_running(False))
            self.root.after(0, lambda: self.progress_var.set(0))
            self.root.after(0, lambda: self.status_label.config(text=t["ready"]))

    def _do_decrypt(self):
        t = LANG[self.lang]
        try:
            key = self.key_var.get().strip().encode()
            fernet = Fernet(key)
            files = self._collect_files(self.selected_folder)
            total = len(files)
            count = 0

            for i, fpath in enumerate(files):
                self._update_progress(i, total)
                try:
                    with open(fpath, "rb") as f:
                        data = f.read()
                    decrypted = fernet.decrypt(data)
                    with open(fpath, "wb") as f:
                        f.write(decrypted)
                    count += 1
                except Exception:
                    self.root.after(0, lambda: messagebox.showerror(
                        t["error"], t["key_error"]))
                    break

            self._update_progress(total, total)
            self.root.after(0, lambda: messagebox.showinfo(
                t["dec_btn"], t["dec_done"].format(count)))
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror(
                t["error"], t["dec_error"].format(str(e))))
        finally:
            self.root.after(0, lambda: self._set_running(False))
            self.root.after(0, lambda: self.progress_var.set(0))
            self.root.after(0, lambda: self.status_label.config(text=t["ready"]))


def main():
    root = tk.Tk()

    try:
        root.tk.call("tk", "scaling", 1.0)
    except Exception:
        pass

    app = LockTabApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
