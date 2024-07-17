import win32com.client
 
# Create an Outlook application object
outlook = win32com.client.Dispatch('outlook.application')
 
# Create a new email item
mail = outlook.CreateItem(0)
mail.To = 'correo a enviar'
mail.Subject = 'Asunto'
mail.Body = 'Cuerpo'
mail.Send()
