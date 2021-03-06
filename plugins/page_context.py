# -*- coding: utf-8 -*-


class MenuItem:
    def __init__(self, url, title, context, css="", children=()):
        self.url = url
        self.title = title
        self.context = context
        self.css = css
        self.children = children


def preBuildPage(page, context, data):
    """
    Updates the context of the page to include: the page itself as {{ CURRENT_PAGE }}
    """

    # This will run for each page that Cactus renders.
    # Any changes you make to context will be passed to the template renderer for this page.

    menu = (
        MenuItem("/news", "News", "Navigation bar link to Mixxx News page."),
        MenuItem(
            "/discover",
            "Discover",
            "Navigation bar link to Mixxx discover page.",
            children=(
                MenuItem(
                    "/features",
                    "Features",
                    "Navigation bar link to Mixxx features page.",
                ),
                MenuItem(
                    "/screenshots",
                    "Screenshots",
                    "Navigation bar link to Mixxx Screenshots page.",
                ),
                MenuItem(
                    "/press",
                    "Press",
                    "Navigation bar link to Mixxx Press page",
                ),
                MenuItem(
                    "/contact",
                    "Contact & Team",
                    "Navigation bar link to Mixxx contact page.",
                ),
            ),
        ),
        MenuItem(
            "/support",
            "Support & Community",
            "Navigation bar link to Mixxx support page.",
            children=(
                MenuItem(
                    "/manual/latest",
                    "Manual",
                    "Navigation bar link to Mixxx Manual.",
                ),
                MenuItem(
                    "https://mixxx.discourse.group/",
                    "Forums",
                    "Navigation bar link to Mixxx Forums.",
                ),
                MenuItem(
                    "https://github.com/mixxxdj/mixxx/wiki",
                    "Wiki",
                    "Navigation bar link to Mixxx Wiki.",
                ),
                MenuItem(
                    "/get-involved",
                    "Get Involved",
                    "Navigation bar link to Mixxx Get Involved page.",
                ),
            ),
        ),
    )

    extra = {
        "CURRENT_PAGE": page,
        # Add your own dynamic context elements here!
        "NAV_MENU": menu,
    }

    context.update(extra)
    return context, data
