from docx import Document
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt #����
from docx.oxml.ns import qn #���ĸ�ʽ

#�ж�Unicode�ַ��Ƿ�������
def is_number(uchar):
    if uchar >= u'\u0030' and uchar<=u'\u0039':
       return True
    else:
       return False

def para_change(source_document, target_document):
    for paragraph in source_document.paragraphs:

        #���word����
        text = paragraph.text
        p = target_document.add_paragraph(u'')
        run = p.add_run(text)

        #���ö�����������
        run.font.name = u'����'
        run.element.rPr.rFonts.set(qn('w:eastAsia'),u'����')
        if (is_number(text)) :
            #���������С
            run.font.size = Pt(8)
        else:
            run.font.size = Pt(11)
        '''
        i = i + 1
        if (i > 100):
            break
        '''

        #�����м��
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after =Pt(0)

if __name__ == '__main__':
    #for i in range(1, 19) :
    path = 'C:\\Users\\������\\Desktop\\�½��ļ���\\������ ����ѧ5.docx' 
        #path = path + str(i) + '.docx'
    source_document = Document(path)
    target_document = Document()
    para_change(source_document, target_document)
    target_document.save('a������ ����ѧ5.docx')
