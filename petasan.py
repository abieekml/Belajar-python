import tkinter as tk
import random
import math
import time
from datetime import datetime
from threading import Thread

class Particle:
    def __init__(self, canvas, x, y, color, speed):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        self.radius = 3
        self.speed = speed
        self.angle = random.uniform(0, 2 * math.pi)
        self.vx = math.cos(self.angle) * self.speed
        self.vy = math.sin(self.angle) * self.speed
        self.lifetime = 100
        self.gravity = 0.05
        self.id = canvas.create_oval(
            x - self.radius, y - self.radius,
            x + self.radius, y + self.radius,
            fill=self.color, outline=self.color
        )
        
    def update(self):
        if self.lifetime <= 0:
            self.canvas.delete(self.id)
            return False
            
        self.x += self.vx
        self.y += self.vy
        self.vy += self.gravity
        self.lifetime -= 1
        
        # Update posisi partikel di canvas
        self.canvas.move(self.id, self.vx, self.vy)
        
        # Kurangi opacity dengan mengganti warna
        alpha = int(self.lifetime * 255 / 100)
        if alpha < 0:
            alpha = 0
        
        # Sesuaikan warna berdasarkan lifetime
        r, g, b = self.canvas.winfo_rgb(self.color)
        r, g, b = r // 256, g // 256, b // 256
        brightness = self.lifetime / 100
        new_color = f'#{int(r * brightness):02x}{int(g * brightness):02x}{int(b * brightness):02x}'
        self.canvas.itemconfig(self.id, fill=new_color, outline=new_color)
        
        return True

class Firework:
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.reset()
        
    def reset(self):
        self.x = random.randint(100, self.width - 100)
        self.y = self.height
        self.speed = random.uniform(3, 7)
        self.colors = ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff', '#00ffff', '#ffffff']
        self.color = random.choice(self.colors)
        self.particles = []
        self.exploded = False
        self.target_height = random.randint(50, self.height - 200)
        self.id = self.canvas.create_rectangle(
            self.x - 1, self.y - 5,
            self.x + 1, self.y,
            fill=self.color, outline=self.color
        )
        self.trail_id = self.canvas.create_oval(
            self.x - 1, self.y + 5 - 2,
            self.x + 1, self.y + 5 + 2,
            fill='#ffcc00', outline='#ffcc00'
        )
    
    def update(self):
        if not self.exploded:
            self.y -= self.speed
            self.canvas.move(self.id, 0, -self.speed)
            self.canvas.move(self.trail_id, 0, -self.speed)
            
            if self.y <= self.target_height:
                self.explode()
                return True
        else:
            # Update all particles
            particles_to_remove = []
            for i, particle in enumerate(self.particles):
                if not particle.update():
                    particles_to_remove.append(i)
            
            # Remove dead particles
            for i in sorted(particles_to_remove, reverse=True):
                del self.particles[i]
            
            # If all particles are gone, reset the firework
            if len(self.particles) == 0:
                self.reset()
                return True
                
        return False
    
    def explode(self):
        self.exploded = True
        self.canvas.delete(self.id)
        self.canvas.delete(self.trail_id)
        
        num_particles = random.randint(30, 70)
        for _ in range(num_particles):
            particle_color = random.choice(self.colors)
            speed = random.uniform(1.5, 4)
            self.particles.append(Particle(self.canvas, self.x, self.y, particle_color, speed))

class NewYearFireworksApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Petasan Tahun Baru")
        
        # Ukuran layar
        self.width = 800
        self.height = 600
        
        # Membuat canvas
        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg='black')
        self.canvas.pack(expand=True, fill=tk.BOTH)
        
        # Variabel untuk kontrol
        self.running = True
        self.countdown_active = True
        self.countdown_seconds = 5
        self.fireworks = []
        self.max_fireworks = 10
        
        # Tombol kontrol
        frame = tk.Frame(root)
        frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.add_firework_btn = tk.Button(frame, text="Tambah Petasan", command=self.add_firework)
        self.add_firework_btn.pack(side=tk.LEFT, padx=5)
        
        self.restart_btn = tk.Button(frame, text="Mulai Ulang", command=self.restart)
        self.restart_btn.pack(side=tk.LEFT, padx=5)
        
        self.quit_btn = tk.Button(frame, text="Keluar", command=self.quit_app)
        self.quit_btn.pack(side=tk.RIGHT, padx=5)
        
        # Label untuk informasi
        self.info_label = tk.Label(frame, text=f"Petasan: 0/{self.max_fireworks}")
        self.info_label.pack(side=tk.RIGHT, padx=20)
        
        # Bind keyboard shortcuts
        self.root.bind("<space>", lambda e: self.add_firework())
        self.root.bind("r", lambda e: self.restart())
        self.root.bind("<Escape>", lambda e: self.quit_app())
        
        # Mulai countdown
        self.countdown_text_id = self.canvas.create_text(
            self.width // 2, self.height // 2,
            text=str(self.countdown_seconds),
            font=("Arial", 80, "bold"),
            fill="white"
        )
        
        # Tahun Baru teks
        current_year = datetime.now().year
        self.new_year_text = f"SELAMAT TAHUN BARU {current_year + 1}!"
        
        # Judul
        self.title_text_id = self.canvas.create_text(
            self.width // 2, 30,
            text=self.new_year_text,
            font=("Arial", 24, "bold"),
            fill=self.random_color()
        )
        self.canvas.itemconfig(self.title_text_id, state='hidden')
        
        # Mulai thread untuk update
        self.update_thread = Thread(target=self.update_loop)
        self.update_thread.daemon = True
        self.update_thread.start()
        
        # Mulai countdown
        self.countdown_start = time.time()
        self.root.after(100, self.update_countdown)
    
    def random_color(self):
        colors = ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff', '#00ffff']
        return random.choice(colors)
    
    def update_countdown(self):
        if not self.countdown_active:
            return
            
        elapsed = time.time() - self.countdown_start
        remaining = self.countdown_seconds - elapsed
        
        if remaining <= 0:
            self.countdown_active = False
            self.canvas.itemconfig(self.countdown_text_id, text=self.new_year_text)
            self.canvas.itemconfig(self.title_text_id, state='normal')
            
            # Mulai pertunjukan petasan
            for _ in range(5):
                self.add_firework()
                
            # Sembunyikan countdown setelah beberapa detik
            self.root.after(2000, lambda: self.canvas.itemconfig(self.countdown_text_id, state='hidden'))
        else:
            self.canvas.itemconfig(self.countdown_text_id, text=str(int(remaining) + 1))
            self.root.after(100, self.update_countdown)
    
    def update_loop(self):
        while self.running:
            # Update fireworks
            fireworks_to_update = list(range(len(self.fireworks)))
            for i in fireworks_to_update:
                if i < len(self.fireworks):  # Pastikan index masih valid
                    self.fireworks[i].update()
            
            # Ubah warna judul secara berkala
            if not self.countdown_active and random.random() < 0.05:
                self.canvas.itemconfig(self.title_text_id, fill=self.random_color())
                
            time.sleep(0.03)  # ~30 FPS
    
    def add_firework(self):
        if len(self.fireworks) < self.max_fireworks and not self.countdown_active:
            self.fireworks.append(Firework(self.canvas, self.width, self.height))
            self.info_label.config(text=f"Petasan: {len(self.fireworks)}/{self.max_fireworks}")
    
    def restart(self):
        # Hapus semua petasan
        for firework in self.fireworks:
            if hasattr(firework, 'id') and firework.id:
                self.canvas.delete(firework.id)
            if hasattr(firework, 'trail_id') and firework.trail_id:
                self.canvas.delete(firework.trail_id)
            for particle in firework.particles:
                if hasattr(particle, 'id') and particle.id:
                    self.canvas.delete(particle.id)
        
        self.fireworks = []
        self.info_label.config(text=f"Petasan: 0/{self.max_fireworks}")
        
        # Reset countdown
        self.countdown_active = True
        self.countdown_start = time.time()
        self.canvas.itemconfig(self.countdown_text_id, state='normal')
        self.canvas.itemconfig(self.title_text_id, state='hidden')
        self.update_countdown()
    
    def quit_app(self):
        self.running = False
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = NewYearFireworksApp(root)
    root.mainloop()