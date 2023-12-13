import logging
import re
import csv
from openpyxl import Workbook
from openpyxl.styles import Font
from tempfile import NamedTemporaryFile


from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.http import Http404, HttpResponse, QueryDict
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.core.exceptions import PermissionDenied

from dojo.filters import ReportFindingFilter, EndpointReportFilter, \
    EndpointFilter
from dojo.forms import ReportOptionsForm
from dojo.models import Product_Type, Finding, Product, Engagement, Test, \
    Dojo_User, Endpoint, Risk_Acceptance
from dojo.reports.widgets import CoverPage, PageBreak, TableOfContents, WYSIWYGContent, FindingList, EndpointList, \
    CustomReportJsonForm, ReportOptions, report_widget_factory
from dojo.utils import get_page_items, add_breadcrumb, get_system_setting, get_period_counts_legacy, Product_Tab, \
    get_words_for_field
from dojo.authorization.authorization_decorators import user_is_authorized
from dojo.authorization.roles_permissions import Permissions
from dojo.authorization.authorization import user_has_permission_or_403
from dojo.finding.queries import get_authorized_findings
from dojo.finding.views import BaseListFindings

