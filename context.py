from abc import ABC, abstractmethod
from functools import cached_property
from typing import Dict, Iterable, Optional


class ContextInterface(ABC):
    @cached_property
    def desc(self) -> Optional[str]:
        return "This tool allows you to modify any game file at the discretion of the provided context.\n"

    @cached_property
    def prerequisites(self) -> Optional[str]:
        return "Verify integrity of your game files.\n"

    @cached_property
    def success(self) -> Optional[str]:
        return "Files have been successfully modified.\n"

    @cached_property
    @abstractmethod
    def filenames(self) -> Iterable[str]:
        pass

    @cached_property
    @abstractmethod
    def directories_chain(self) -> Iterable[str]:
        pass

    @cached_property
    @abstractmethod
    def replacements(self) -> Dict[str, str]:
        pass


class KF1Context(ContextInterface):
    @cached_property
    def desc(self) -> Optional[str]:
        return "In non-Russian versions of Killing Floor, all Cyrillic letters are rendered as tildes (~).\n" \
               "Because some Slavic-speaking users play a non-Russian version of the game\n" \
               "(possibly due to poor localisation and other reasons), players may wish to enable " \
               "Cyrillic language support.\n"

    @cached_property
    def prerequisites(self) -> Optional[str]:
        return "In the Steam library, ensure that the language setting of Killing Floor is not Russian.\n"

    @cached_property
    def success(self) -> Optional[str]:
        return "\nThe patch has been successfully applied.\n" \
               "Now you can mount and load MLGs with your eastern slavic comrades.\n"

    @cached_property
    def filenames(self) -> Iterable[str]:
        return (
            "Engine.int",
            "GUI2K4.int",
            "KFMod.int",
            "ROEngine.int",
            "UnrealGame.int",
            "XInterface.int"
        )

    @cached_property
    def directories_chain(self) -> Iterable[str]:
        return (
            "steamapps",
            "common",
            "killingfloor",
            "System"
        )

    @cached_property
    def replacements(self) -> Dict[str, str]:
        return {
            "ROFonts.ROBtsrmVr": "ROFonts_RUS.ROArial",
            "ROFontsTwo.ROArial24DS": "ROFonts_Rus.ROArial24",
            "ROFontsTwo.ROArial22DS": "ROFonts_Rus.ROArial22",
            "ROFontsTwo.ROArial18DS": "ROFonts_Rus.ROArial18",
            "ROFontsTwo.ROArial14DS": "ROFonts_Rus.ROArial14",
            "ROFontsTwo.ROArial12DS": "ROFonts_Rus.ROArial12",
            "ROFontsTwo.ROArial9DS": "ROFonts_Rus.ROArial9",
            "ROFontsTwo.ROArial7DS": "ROFonts_Rus.ROArial7"
        }
