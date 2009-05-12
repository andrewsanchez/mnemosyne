#
# SM2_controller_cramming.py <Peter.Bienstman@UGent.be>
#

from mnemosyne.libmnemosyne.component_manager import review_widget
from mnemosyne.libmnemosyne.ui_controllers_review.SM2_controller \
     import SM2Controller
from mnemosyne.libmnemosyne.component_manager import _


class SM2ControllerCramming(SM2Controller):

    def update_grades_area(self):
        w = review_widget()
        w.enable_grades(self.grades_enabled)
        if self.grades_enabled:
            w.set_default_grade(5)