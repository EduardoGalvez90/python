import tkinter as tk
from tkinter import scrolledtext, ttk
from chatbot import responder

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🍽️ Chatbot Comida Rapida")
        self.root.geometry("700x600")
        self.root.configure(bg="#fffef5")  # Fondo suave

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure("Yellow.TButton", font=("Segoe UI", 11), padding=6, background="#f7c948", foreground="black")
        self.style.map("Yellow.TButton",
                       background=[("active", "#f4b400")],
                       foreground=[("active", "#000000")])

        self.style.configure("Option.TButton", font=("Segoe UI", 10), padding=6, background="#fff3cd", foreground="#856404")
        self.style.map("Option.TButton",
                       background=[("active", "#ffe8a1")])

        self.label_title = ttk.Label(self.root, text="Asistente Comida Rapida 🤖", font=("Segoe UI", 20, "bold"), background="#fffef5")
        self.label_title.pack(pady=10)

        self.chat_area = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, state='disabled', font=("Segoe UI", 12),
            bg="#fff9e6", relief=tk.FLAT, bd=3, highlightbackground="#f7c948",
            highlightthickness=1
        )
        self.chat_area.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        self.frame_bottom = tk.Frame(self.root, bg="#fffef5")
        self.frame_bottom.pack(padx=20, pady=(0,10), fill=tk.X)

        self.entry = ttk.Entry(self.frame_bottom, width=70)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.entry.bind("<Return>", self.enviar_mensaje)

        self.btn_enviar = ttk.Button(self.frame_bottom, text="Enviar", style="Yellow.TButton", command=self.enviar_mensaje)
        self.btn_enviar.pack(side=tk.RIGHT)

        self.opciones_frame = tk.Frame(self.root, bg="#fffef5")
        self.opciones_frame.pack(padx=20, pady=(0, 10), fill=tk.X)

        self.mostrar_opciones(["Comida Rapida", "Recomendaciones", "Comida saludable", "Snack Saludable"])

        self.agregar_texto("¡Hola! Soy tu asistente de comidas rápidas 🍟. Te ayudaré a elegir opciones deliciosas, económicas y al instante. ¿Qué deseas hoy?", es_bot=True)

    def agregar_texto(self, mensaje, es_bot=False):
        self.chat_area['state'] = 'normal'
        if es_bot:
            self.chat_area.insert(tk.END, f"\n🤖 Chatbot:\n", 'bot')
            self.chat_area.insert(tk.END, f"  {mensaje}\n", 'bot_mensaje')
        else:
            self.chat_area.insert(tk.END, f"\n👤 Tú:\n", 'usuario')
            self.chat_area.insert(tk.END, f"      {mensaje}\n", 'usuario_mensaje')
        self.chat_area['state'] = 'disabled'
        self.chat_area.yview(tk.END)

    def enviar_mensaje(self, event=None):
        user_input = self.entry.get().strip()
        if not user_input:
            return
        self.agregar_texto(user_input, es_bot=False)
        self.entry.delete(0, tk.END)

        respuesta = responder(user_input)
        self.agregar_texto(respuesta, es_bot=True)
        self.mostrar_opciones(["Presupuesto bajo ", "Vegetariano", "Receta"])

    def mostrar_opciones(self, opciones):
        for widget in self.opciones_frame.winfo_children():
            widget.destroy()

        for opcion in opciones:
            btn = ttk.Button(self.opciones_frame, text=opcion, style="Option.TButton", command=lambda opt=opcion: self.seleccionar_opcion(opt))
            btn.pack(side=tk.LEFT, padx=5)

    def seleccionar_opcion(self, opcion):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, opcion)
        self.enviar_mensaje()

if __name__ == "__main__":
    root = tk.Tk()

    app = ChatbotApp(root)

    app.chat_area.tag_config('bot', foreground='#4a90e2', font=("Segoe UI", 10, "bold"), justify='left')
    app.chat_area.tag_config('bot_mensaje', foreground='#000000', font=("Segoe UI", 12), lmargin1=10, lmargin2=10)
    app.chat_area.tag_config('usuario', foreground='#7f8c8d', font=("Segoe UI", 10, "bold"), justify='right')
    app.chat_area.tag_config('usuario_mensaje', foreground='#2c3e50', font=("Segoe UI", 12, "italic"), justify='right', rmargin=10)

    root.mainloop()
