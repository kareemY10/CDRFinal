import win32com.client




def DisableMacros(path_to_file):
    # open excel app and the workbook
    xlApp = win32com.client.Dispatch("Excel.Application")
    xlwb = xlApp.Workbooks.Open(path_to_file)
    # ITERATE THROUGH EACH VB COMPONENT (CLASS MODULE, STANDARD MODULE, USER FORMS)
    try:    
        for i in xlwb.VBProject.VBComponents:        
            xlmodule = xlwb.VBProject.VBComponents(i.Name)
            if xlmodule.Type in [1, 2, 3]:            
                xlwb.VBProject.VBComponents.Remove(xlmodule)

    except Exception as e:
        print(e)
    finally:    
        # CLOSE AND SAVE AND UNINITIALIZE APP
        print('==================Successfully Removed Marcos From excel File=====================')
        xlwb.Close(True)
        xlApp.Quit
        xlApp = None
