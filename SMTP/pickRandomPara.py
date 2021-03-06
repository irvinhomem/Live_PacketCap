import random
import logging
import linecache

class PickRandomParagraph(object):

    def __init__(self):
        # Configure Logging
        logging.basicConfig(level=logging.INFO)
        #logging.basicConfig(level=logging.WARNING)
        self.logger = logging.getLogger(__name__)
        #self.logger.setLevel(logging.INFO)
        self.logger.setLevel(logging.DEBUG)
        #self.logger.setLevel(logging.WARNING)

        self.text_file = 'Alice-in-Wonderland-Carroll.txt'

    def read_single_random_line(self):
        lines = random.choice(open(self.text_file, 'r').readlines())
        self.logger.debug('Lines:')
        self.logger.debug('**: %s' % lines)

    def get_paragraph_line_number_starts(self,txt_f):
        paragraph_starts = []
        my_file = open(txt_f, 'r')
        for count, line in enumerate(my_file):
            # logger.debug('COUNT: %i' % count)
            # logger.debug('**LINE 1: %s' % line)

            # try:
            line1 = linecache.getline(self.text_file, count + 1)
            #logger.debug('Line: %s' % str(line1))
            line2 = linecache.getline(self.text_file, count + 2)
            #logger.debug('Line: %s' % str(line2))
            line3 = linecache.getline(self.text_file, count + 3)
            #logger.debug('Line: %s' % str(line3))

            if line1.endswith('\n') and line2.startswith('\n'):
                if not line3.startswith('\n'):
                    paragraph_starts.append(count+3)
                    #logger.debug('COUNT +3 (Line number [1-start]): %s' % str(count+3))
                    self.logger.debug('Para start: %s' % str(linecache.getline(self.text_file, count+3)))
            # except:
            #     logger.debug('EOL or some other error')

        # logger.debug('Paragraph starts list length: %i' % len(paragraph_starts))
        # logger.debug('Paragraph 1 line num: %i' % paragraph_starts[0])
        # logger.debug('Paragraph 2 line num: %i' % paragraph_starts[1])
        # logger.debug('Paragraph 3 line num: %i' % paragraph_starts[2])
        # logger.debug('Paragraph 10 line num: %i' % paragraph_starts[9])

        return paragraph_starts

    def pick_random_paragraph(self, para_starts_list):
        selected_para_line_num = random.choice(para_starts_list)
        self.logger.debug('Selected Paragraph Number: %s' % selected_para_line_num)

        para_index = para_starts_list.index(selected_para_line_num)
        self.logger.debug('Paragraph index: %i' % para_index)
        next_para_num = para_starts_list[para_index+1]
        self.logger.debug('Next Paragraph number: %i' % next_para_num)

        self.logger.debug('LINE %i: %s' % (selected_para_line_num, str(linecache.getline(self.text_file, selected_para_line_num))))

        word_list = ['Alice', 'Wonderland', 'Looking', 'Glass', 'Lewis', 'Carroll']
        first_line = str(random.choice(word_list)) + ': '
        my_paragraph = 'Dear Sir/Madam, \n Text from "Alice in Wonderland" by Lewis Carroll: \n\n'
        for count in range(selected_para_line_num, next_para_num-1):
            self.logger.debug('Counter: %i' % count)
            self.logger.debug('LINE %i: %s' % (count, str(linecache.getline(self.text_file, count))))

            # Get only first line
            if count == selected_para_line_num:
                first_line = first_line + str(linecache.getline(self.text_file, count))

            # Combine lines
            my_paragraph = my_paragraph + (str(linecache.getline(self.text_file, count)))

            self.logger.debug('Paragraph:')
            self.logger.debug('--> %s' % my_paragraph)

        return my_paragraph, first_line

    def get_random_paragraph_text(self):
        para_num_list = self.get_paragraph_line_number_starts(self.text_file)
        the_paragraph = self.pick_random_paragraph(para_num_list)

        return the_paragraph

#paragraph_picker = PickRandomParagraph()


