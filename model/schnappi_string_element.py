class Schnappi_string_element:
    def __init__(self, char, del_after):
        self.char = char
        self.del_after = del_after


    def append_all_after(self, element):
        self.del_after.append( element )


    def get_string(self):
        buff = ''
        buff += self.char
        for element in self.del_after:
            buff += element.get_string()
        return buff