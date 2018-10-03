from __future__ import absolute_import

from pymt.framework.bmi_bridge import bmi_factory

from .bmi import BmiKuMethod

BmiKuMethod = bmi_factory(BmiKuMethod)

del bmi_factory
