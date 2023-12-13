from django.urls import re_path

from dojo.finding import views

urlpatterns = [
    # CRUD operations
    re_path(
        r'^finding/(?P<finding_id>\d+)$',
        views.ViewFinding.as_view(),
        name='view_finding'
    ),
    re_path(
        r'^finding/(?P<finding_id>\d+)/edit$',
        views.EditFinding.as_view(),
        name='edit_finding'
    ),
    re_path(
        r'^finding/(?P<finding_id>\d+)/delete$',
        views.DeleteFinding.as_view(),
        name='delete_finding'
    ),
    # Listing operations
    re_path(
        r'^finding$',
        views.ListFindings.as_view(),
        name='all_findings'
    ),
    re_path(
        r'^finding/open$',
        views.ListOpenFindings.as_view(),
        name='open_findings'
    ),
    re_path(
        r'^finding/verified$',
        views.ListVerifiedFindings.as_view(),
        name='verified_findings'
    ),
    re_path(
        r'^finding/closed$',
        views.ListClosedFindings.as_view(),
        name='closed_findings'
    ),
    re_path(
        r'^finding/accepted$',
        views.ListAcceptedFindings.as_view(),
        name='accepted_findings'
    ),
    re_path(
        r'^product/(?P<product_id>\d+)/finding/open$',
        views.ListOpenFindings.as_view(),
        name='product_open_findings'
    ),
    re_path(
        r'^product/(?P<product_id>\d+)/findings$',
        views.ListOpenFindings.as_view(),
        name='view_product_findings_old'
    ),
    re_path(
        r'^product/(?P<product_id>\d+)/finding/verified$',
        views.ListVerifiedFindings.as_view(),
        name='product_verified_findings'
    ),
    re_path(
        r'^product/(?P<product_id>\d+)/finding/out_of_scope$',
        views.ListOutOfScopeFindings.as_view(),
        name='product_out_of_scope_findings'
    ),
    re_path(
        r'^product/(?P<product_id>\d+)/finding/inactive$',
        views.ListInactiveFindings.as_view(),
        name='product_inactive_findings'
    ),
    re_path(
        r'^product/(?P<product_id>\d+)/finding/all$',
        views.ListFindings.as_view(),
        name='product_all_findings'
    ),
    re_path(
        r'^product/(?P<product_id>\d+)/finding/closed$',
        views.ListClosedFindings.as_view(),
        name='product_closed_findings'
    ),
    re_path(
        r'^product/(?P<product_id>\d+)/finding/false_positive$',
        views.ListFalsePositiveFindings.as_view(),
        name='product_false_positive_findings'
    ),
    re_path(
        r'^product/(?P<product_id>\d+)/finding/accepted$',
        views.ListAcceptedFindings.as_view(),
        name='product_accepted_findings'
    ),
    re_path(
        r'^engagement/(?P<engagement_id>\d+)/finding/open$',
        views.ListOpenFindings.as_view(),
        name='engagement_open_findings'
    ),
    re_path(
        r'^engagement/(?P<engagement_id>\d+)/finding/closed$',
        views.ListClosedFindings.as_view(),
        name='engagement_closed_findings'
    ),
    re_path(
        r'^engagement/(?P<engagement_id>\d+)/finding/verified$',
        views.ListVerifiedFindings.as_view(),
        name='engagement_verified_findings'
    ),
    re_path(
        r'^engagement/(?P<engagement_id>\d+)/finding/accepted$',
        views.ListAcceptedFindings.as_view(),
        name='engagement_accepted_findings'
    ),
    re_path(
        r'^engagement/(?P<engagement_id>\d+)/finding/all$',
        views.ListFindings.as_view(),
        name='engagement_all_findings'
    ),
    #  findings
    re_path(r'^finding/bulk$', views.finding_bulk_update_all,
        name='finding_bulk_update_all'),
    re_path(r'^product/(?P<pid>\d+)/finding/bulk_product$', views.finding_bulk_update_all,
        name='finding_bulk_update_all_product'),
    # re_path(r'^test/(?P<tid>\d+)/bulk', views.finding_bulk_update_all,
    #     name='finding_bulk_update_all_test'),
    re_path(r'^finding/(?P<fid>\d+)/touch$',
        views.touch_finding, name='touch_finding'),
    re_path(r'^finding/(?P<fid>\d+)/simple_risk_accept$',
        views.simple_risk_accept, name='simple_risk_accept_finding'),
    re_path(r'^finding/(?P<fid>\d+)/simple_risk_unaccept$',
        views.risk_unaccept, name='risk_unaccept_finding'),
    re_path(r'^finding/(?P<fid>\d+)/request_review$',
        views.request_finding_review, name='request_finding_review'),
    re_path(r'^finding/(?P<fid>\d+)/review$',
        views.clear_finding_review, name='clear_finding_review'),
    re_path(r'^finding/(?P<fid>\d+)/copy$',
        views.copy_finding, name='copy_finding'),
    re_path(r'^finding/(?P<fid>\d+)/apply_cwe$',
        views.apply_template_cwe, name='apply_template_cwe'),
    re_path(r'^finding/(?P<fid>\d+)/mktemplate$', views.mktemplate,
        name='mktemplate'),
    re_path(r'^finding/(?P<fid>\d+)/find_template_to_apply$', views.find_template_to_apply,
        name='find_template_to_apply'),
    re_path(r'^finding/(?P<tid>\d+)/(?P<fid>\d+)/choose_finding_template_options$', views.choose_finding_template_options,
        name='choose_finding_template_options'),
    re_path(r'^finding/(?P<fid>\d+)/(?P<tid>\d+)/apply_template_to_finding$',
        views.apply_template_to_finding, name='apply_template_to_finding'),
    re_path(r'^finding/(?P<fid>\d+)/close$', views.close_finding,
        name='close_finding'),
    re_path(r'^finding/(?P<fid>\d+)/defect_review$',
        views.defect_finding_review, name='defect_finding_review'),
    re_path(r'^finding/(?P<fid>\d+)/open$', views.reopen_finding,
        name='reopen_finding'),
    re_path(r'^finding/image/(?P<token>[^/]+)$', views.download_finding_pic,
        name='download_finding_pic'),
    re_path(r'^finding/(?P<fid>\d+)/merge$',
        views.merge_finding_product, name='merge_finding'),
    re_path(r'^product/(?P<pid>\d+)/merge$', views.merge_finding_product,
        name='merge_finding_product'),
    re_path(r'^finding/(?P<duplicate_id>\d+)/duplicate/(?P<original_id>\d+)$',
        views.mark_finding_duplicate, name='mark_finding_duplicate'),
    re_path(r'^finding/(?P<duplicate_id>\d+)/duplicate/reset$',
        views.reset_finding_duplicate_status, name='reset_finding_duplicate_status'),
    re_path(r'^finding/(?P<finding_id>\d+)/original/(?P<new_original_id>\d+)$',
        views.set_finding_as_original, name='set_finding_as_original'),
    re_path(r'^finding/(?P<fid>\d+)/remediation_date$', views.remediation_date,
        name='remediation_date'),
    # stub findings
    re_path(r'^stub_finding/(?P<tid>\d+)/add$',
        views.add_stub_finding, name='add_stub_finding'),
    re_path(r'^stub_finding/(?P<fid>\d+)/promote$',
        views.promote_to_finding, name='promote_to_finding'),
    re_path(r'^stub_finding/(?P<fid>\d+)/delete$',
        views.delete_stub_finding, name='delete_stub_finding'),

    # template findings

    re_path(r'^template$', views.templates,
        name='templates'),
    re_path(r'^template/add$', views.add_template,
        name='add_template'),
    re_path(r'^template/(?P<tid>\d+)/edit$',
        views.edit_template, name='edit_template'),
    re_path(r'^template/(?P<tid>\d+)/delete$',
        views.delete_template, name='delete_template'),
    re_path(r'^template/export$',
        views.export_templates_to_json, name='export_template'),

    re_path(r'^finding/(?P<fid>\d+)/jira/unlink$', views.unlink_jira, name='finding_unlink_jira'),
    re_path(r'^finding/(?P<fid>\d+)/jira/push$', views.push_to_jira, name='finding_push_to_jira'),
    # re_path(r'^finding/(?P<fid>\d+)/jira/push', views.finding_link_to_jira, name='finding_link_to_jira'),

]
