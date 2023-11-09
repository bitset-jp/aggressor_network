import enum

class TextColor(enum.Enum):
    # Reset
    NONE='\033[0m'       # Text Reset

    # Regular Colors
    BLACK='\033[0;30m'        # Black
    RED='\033[0;31m'          # Red
    GREEN='\033[0;32m'        # Green
    YELLOW='\033[0;33m'       # Yellow
    BLUE='\033[0;34m'         # Blue
    PURPLE='\033[0;35m'       # Purple
    CYAN='\033[0;36m'         # Cyan
    WHITE='\033[0;37m'        # White

    # Bold
    B_BLACK='\033[1;30m'       # Black
    B_RED='\033[1;31m'         # Red
    B_GREEN='\033[1;32m'       # Green
    B_YELLOW='\033[1;33m'      # Yellow
    B_BLUE='\033[1;34m'        # Blue
    B_PURPLE='\033[1;35m'      # Purple
    B_CYAN='\033[1;36m'        # Cyan
    B_WHITE='\033[1;37m'       # White

    # # Underline
    # U_BLACK='\033[4;30m'       # Black
    # U_RED='\033[4;31m'         # Red
    # U_GREEN='\033[4;32m'       # Green
    # U_YELLOW='\033[4;33m'      # Yellow
    # U_BLUE='\033[4;34m'        # Blue
    # U_PURPLE='\033[4;35m'      # Purple
    # U_CYAN='\033[4;36m'        # Cyan
    # U_WHITE='\033[4;37m'       # White

    # # Background
    # On_Black='\033[40m'       # Black
    # On_Red='\033[41m'         # Red
    # On_Green='\033[42m'       # Green
    # On_Yellow='\033[43m'      # Yellow
    # On_Blue='\033[44m'        # Blue
    # On_Purple='\033[45m'      # Purple
    # On_Cyan='\033[46m'        # Cyan
    # On_White='\033[47m'       # White

    # # High Intensity
    # IBlack='\033[0;90m'       # Black
    # IRed='\033[0;91m'         # Red
    # IGreen='\033[0;92m'       # Green
    # IYellow='\033[0;93m'      # Yellow
    # IBlue='\033[0;94m'        # Blue
    # IPurple='\033[0;95m'      # Purple
    # ICyan='\033[0;96m'        # Cyan
    # IWhite='\033[0;97m'       # White

    # # Bold High Intensity
    # BIBlack='\033[1;90m'      # Black
    # BIRed='\033[1;91m'        # Red
    # BIGreen='\033[1;92m'      # Green
    # BIYellow='\033[1;93m'     # Yellow
    # BIBlue='\033[1;94m'       # Blue
    # BIPurple='\033[1;95m'     # Purple
    # BICyan='\033[1;96m'       # Cyan
    # BIWhite='\033[1;97m'      # White

    # # High Intensity backgrounds
    # On_IBlack='\033[0;100m'   # Black
    # On_IRed='\033[0;101m'     # Red
    # On_IGreen='\033[0;102m'   # Green
    # On_IYellow='\033[0;103m'  # Yellow
    # On_IBlue='\033[0;104m'    # Blue
    # On_IPurple='\033[0;105m'  # Purple
    # On_ICyan='\033[0;106m'    # Cyan
    # On_IWhite='\033[0;107m'   # White

SAVE_DIR = f'{__file__}/../res/new_help/'

class HelpFile():
    def __init__(self, name):
        self.name: str = name
        self.texts: list[str] = []
    
    def save(self):
        with open(f'{SAVE_DIR}{self.name}.txt', 'w') as f:
            f.writelines(self.texts)
    
    def _write_line(self, text: str):
        self.texts.append(text)

    def _write_header(self, header: str):
        self._write_line(f'{header}')

    def _write_section(self, section_name: str, texts: list[str]):
        self._write_line(f'\t{section_name}:')
        for text in texts:
            self._write_line(text)

    @staticmethod
    def get_colored_text(text: str, color: TextColor) -> str:
        return f'{color.value}{text}{TextColor.NONE.value}'
    