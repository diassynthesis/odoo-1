# Copyright (C) 2020-2023 Artem Shurshilov <shurshilov.a@yandex.ru>
# License OPL-1.0
{
    "name": "Mail message Firebase push notifications",
    "summary": """
        Provide free unlimited push notifications and chats odoo mail messaged (discuss, chat, chatter etc...)""",
    "author": "EURO ODOO, Shurshilov Artem",
    "maintainer": "EURO ODOO",
    "website": "https://eurodoo.com",
    "live_test_url": "https://eurodoo.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Mail",
    "version": "16.0.0.2",
    "license": "OPL-1",
    "price": 19,
    "currency": "EUR",
    "images": [
        "static/description/preview.png",
    ],
    # any module necessary for this one to work correctly
    "depends": ["base", "web", "mail"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        # 'views/assets.xml',
        "views/res_users.xml",
        #'views/iap_firebase.xml',
        "views/res_config_settings_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "https://www.gstatic.com/firebasejs/8.6.0/firebase-app.js",
            "https://www.gstatic.com/firebasejs/8.6.0/firebase-messaging.js",
        ],
    },
}
