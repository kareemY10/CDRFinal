import win32com.client
import aspose.words as aw
from aspose import slides

def delete_macro_excel(path_to_file):
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


def delete_macro_word(path_to_file):
    doc=aw.Document(path_to_file)
    project =doc.vba_project
    
    # ITERATE THROUGH EACH VB COMPONENT (CLASS MODULE, STANDARD MODULE, USER FORMS)
    try:    
        for i in list(project.modules):
           project.modules.remove(i)
    except Exception as e:
        print(e)
    finally:    
        # CLOSE AND SAVE AND UNINITIALIZE APP
        print('==================Successfully Removed Marcos From docm File=====================')

def Delete_Macro_PowerPoint (path_to_file):
    with slides.Presentation(path_to_file) as presentation:
        presentation.vba_project.modules.remove(presentation.vba_project.modules[0])
        # Save presentation
        presentation.save("remove-vba-macro.pptm", slides.export.SaveFormat.PPTM)
    
    




# Delete_Macro_PowerPoint('C:\temp\\NAC\\FinalProject\\CDRFP\\CDRFinal\\PTest.pptm')
# delete_macro_word('C:\\temp\\NAC\\FinalProject\\CDRFP\\CDRFinal\\Test.docm')