import PySimpleGUI as sg
import qrcode
from os import remove


# Set UI theme and control names
sg.theme('DarkBlue')
exit_button = 'Exit'
qr_data_input = 'qr data'
qr_code_image = 'qr code'
qr_create_button = 'Create QR Code'
qr_code_filename = 'qrcode.png'

layout = [
    [sg.Text('Enter Text for QR Code Data')],
    [sg.InputText(k=qr_data_input)],
    [sg.Image(k=qr_code_image)],
    [sg.Button(qr_create_button), sg.Button(exit_button)]
]

window = sg.Window('Create QR Code', layout)

# UI starts here
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == exit_button:
        break
    elif event == qr_create_button:
        img = qrcode.make(values[qr_data_input])
        img.save(qr_code_filename)
        window.Element(qr_code_image).Update(
            filename=qr_code_filename, data=qr_data_input, size=img.size)

remove(qr_code_filename)
window.close()
