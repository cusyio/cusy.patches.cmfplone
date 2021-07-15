# -*- coding: utf-8 -*-

from Products.CMFCore.utils import _checkPermission
from Products.CMFCore.utils import getToolByName
from zope.globalrequest import getRequest
from zope.i18n import translate
from zope.i18nmessageid import Message


def enumConfiglets(self, group=None):
    portal = getToolByName(self, "portal_url").getPortalObject()

    # PATCH: Get the correct context
    request = getRequest()
    try:
        obj = request.PUBLISHED.context
    except AttributeError:
        obj = portal

    # PATCH: Use the correct expression context
    # context = createExprContext(self, portal, self)
    context = self._getExprContext(obj)

    res = []
    for a in self.listActions():
        verified = 0
        for permission in a.permissions:
            if _checkPermission(permission, portal):
                verified = 1
        if verified and a.category == group and a.testCondition(context) and a.visible:
            res.append(a.getAction(context))
    # Translate the title for sorting
    if getattr(self, "REQUEST", None) is not None:
        for a in res:
            title = a["title"]
            if not isinstance(title, Message):
                title = Message(title, domain="plone")
            a["title"] = translate(title, context=self.REQUEST)

    def _title(v):
        return v["title"]

    res.sort(key=_title)
    return res


def customPatchHandler(scope, original, replacement):  # noqa: N802
    """Custom handler that preserves original method with a custom name."""
    OLD_NAME = "_old_cusy_patches_cmfplone_{0}".format(original)  # noqa: N806

    if not getattr(scope, OLD_NAME, None):
        setattr(scope, OLD_NAME, getattr(scope, original))

    setattr(scope, original, replacement)
    return
