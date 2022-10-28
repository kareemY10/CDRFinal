from zipfile import ZipFile

exe_extensions = (
                  '.bms','.msi','.ahk','.apk','.jar','.ipa','.run','.cmd','.xbe','.0xe',
                  '.exe','.workflow','.bin','.elf','.8ck','.bat','.sk','.air',
                  '.gadget','.xap','.ac','.widget','.app','.u3p','.pif','.fpa',
                  '.rbf','.mcr','.com','.sh','.tpk','.out','.x86','.73k','.ex_',
                  '.rxe','.command','.xex','.x86_64','.ebs2','.a7r','.plx','.nexe',
                  '.exe1','.pyc','.e_e','.spr','.uvm','.osx','.vexe','.upx','.ore','.ezt'
                  )


compressed_extensions = ('gz','zip','rar','z','7z')

process_extensions = ()


# main function to call the recursive function...
def CleanCompressedFiles(filepath,cleanfile):
    archive = ZipFile(filepath,'r')
    clean_archive  = ZipFile(cleanfile,'w')
    CleanFiles(z_in = archive, z_out = clean_archive)


# recursive function :-
def CleanFiles(z_in : ZipFile, z_out : ZipFile):
    if z_in is None:
        return z_out
    
    for item in z_in.infolist():
        file_name = item.filename
        buffer = z_in.read(file_name)
        file_extension = file_name.split('.')
        if len(file_extension) > 2:
            file_extension = [extension+'.' for extension in file_extension]
            file_extension[-1] = file_extension[-1][:-1]
        file_extension = ''.join(file_extension[1:])  
         
        
    
