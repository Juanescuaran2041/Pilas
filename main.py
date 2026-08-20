import tkinter as tk
from tkinter import messagebox, ttk

class DPIStackInspector():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def isEmpty (self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def to_list (self):
        return list(self.items)


def generar_paquete():

    pass
    

#---Aplicacion---#
class DPIAppSimulator():
    def __init__(self, root):
        self.root = root
        self.root.title = ("Simulador DPI usando la estructura Stack")
        self.root.geometry("820x560")
        self.root.resizable(False, False)

        self.max_depth = 4
        self.stack = DPIStackInspector()
        self.current_packet = []
        self.token_index = 0
 
        self.escenarios = {
            "1. Tráfico legítimo (HTTPS normal)": [
                "OPEN_ETHERNET", "OPEN_IP", "OPEN_TCP", "OPEN_TLS", "OPEN_HTTP",
                "CLOSE_HTTP", "CLOSE_TLS", "CLOSE_TCP", "CLOSE_IP", "CLOSE_ETHERNET"
            ],
            "2. Túnel de evasión (VPN dentro de DNS dentro de HTTPS)": [
                "OPEN_ETHERNET", "OPEN_IP", "OPEN_TCP", "OPEN_TLS", "OPEN_DNS", "OPEN_VPN",
                "CLOSE_VPN", "CLOSE_DNS", "CLOSE_TLS", "CLOSE_TCP", "CLOSE_IP", "CLOSE_ETHERNET"
            ],
            "3. Header falsificado (incoherencia LIFO)": [
                "OPEN_ETHERNET", "OPEN_IP", "OPEN_TCP",
                "CLOSE_IP", 
                "CLOSE_TCP", "CLOSE_ETHERNET"
            ],
            "4. Paquete truncado (capas sin cerrar)": [
                "OPEN_ETHERNET", "OPEN_IP", "OPEN_TCP", "OPEN_HTTP"
            ],
        }

        self.setup()

    def setup(self):
        frame_top = ttk.LabelFrame(self.root, text=" Configuración de la Inspección ", padding=10)
        frame_top.pack(fill="x", padx=10, pady=5)
 
        ttk.Label(frame_top, text="Seleccionar Escenario:").grid(row=0, column=0, sticky="w", padx=5)
 
        self.combo_scenario = ttk.Combobox(frame_top, state="readonly", width=50)
        self.combo_scenario["values"] = list(self.escenarios.keys())
        self.combo_scenario.current(0)
        self.combo_scenario.grid(row=0, column=1, padx=5)
        self.combo_scenario.bind("<<ComboboxSelected>>", self.load_scenario)
 
        ttk.Label(frame_top, text=f"Umbral de profundidad: {self.max_depth}").grid(
            row=0, column=2, padx=15, sticky="w"
        )
 
        frame_controls = ttk.Frame(self.root, padding=5)
        frame_controls.pack(fill="x", padx=10)
 
        self.btn_step = ttk.Button(frame_controls, text="Siguiente Paso ➔", command=self.process_step)
        self.btn_step.pack(side="left", padx=5)
 
        self.btn_reset = ttk.Button(frame_controls, text="Reiniciar Escenario", command=self.load_scenario)
        self.btn_reset.pack(side="left", padx=5)
 
        self.btn_random = ttk.Button(frame_controls, text="🎲 Generar Escenario Aleatorio", command=self.load_random_scenario)
        self.btn_random.pack(side="left", padx=5)
 
        frame_main = ttk.Frame(self.root, padding=10)
        frame_main.pack(fill="both", expand=True, padx=10)
 
        # Stack
        frame_stack = ttk.LabelFrame(frame_main, text=" Estado de la Pila (TOPE arriba) ", padding=10)
        frame_stack.pack(side="left", fill="both", expand=True, padx=(0, 5))
 
        self.list_stack = tk.Listbox(frame_stack, font=("Consolas", 12, "bold"), selectbackground="#e1e1e1")
        self.list_stack.pack(fill="both", expand=True)
 
        # Stream + log
        frame_right = ttk.Frame(frame_main)
        frame_right.pack(side="right", fill="both", expand=True, padx=(5, 0))
 
        frame_stream = ttk.LabelFrame(frame_right, text=" Cadena de Protocolos (Tokens) ", padding=5)
        frame_stream.pack(fill="x", pady=(0, 5))
 
        self.lbl_stream = ttk.Label(frame_stream, text="", font=("Consolas", 10), wraplength=380, justify="left")
        self.lbl_stream.pack(fill="x")
 
        frame_log = ttk.LabelFrame(frame_right, text=" Registro del Firewall (DPI) ", padding=5)
        frame_log.pack(fill="both", expand=True)
 
        self.txt_log = tk.Text(frame_log, font=("Consolas", 9), state="disabled", bg="#1e1e1e", fg="#00ff00", wrap="word")
        self.txt_log.pack(fill="both", expand=True)
 
        self.load_scenario()

    #logic
    def log(self, message):
        self.txt_log.config("")


    


if __name__ == "__main__":
    root = tk.Tk()
    app = DPIAppSimulator(root)
    root.mainloop()


        