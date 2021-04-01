from page_objects import AdminPage, SearchFilter
import pytest


def test_open_home_page(browser):
    AdminPage(browser) \
        .open_admin_page(browser) \
        .check_custom_text_widget_benefits()


def test_create_new_benefit(browser):
    AdminPage(browser) \
        .open_admin_page(browser) \
        .create_new_benefit(cost=100, stock=50, description="Lorem Ipsum is simply dummy text of the printing and "
                                                            "typesetting industry. Lorem Ipsum has been the "
                                                            "industry's standard dummy text ever since the 1500s, "
                                                            "when an unknown printer took a galley of type and "
                                                            "scrambled it to make a type specimen book. It has "
                                                            "survived not only five centuries, but also the leap into "
                                                            "electronic typesetting, remaining essentially unchanged. "
                                                            "It was popularised in the 1960s with the release of "
                                                            "Letraset sheets containing Lorem Ipsum passages, "
                                                            "and more recently with desktop publishing software like "
                                                            "Aldus PageMaker including versions of Lorem Ipsum.",
                            name='TADIRAN SUPREME 777-999')

# @pytest.mark.parametrize('execution_number', range(1))
# def test_go_to_orders_page(browser, execution_number):
#     AdminPage(browser) \
#         .open_admin_page(browser) \
#         .open_page_subscriptions() \
#         .open_page_orders() \
#         .check_custom_text_widget_orders()
#
#
# def test_display_processing_orders(browser):
#     AdminPage(browser) \
#         .open_admin_page(browser)
#     SearchFilter(browser) \
#         .display_processing_order()
#
#
# def test_display_completed_orders(browser):
#     AdminPage(browser) \
#         .open_admin_page(browser)
#     SearchFilter(browser) \
#         .display_completed_order()
#
#
# def test_display_pending_orders(browser):
#     AdminPage(browser) \
#         .open_admin_page(browser)
#     SearchFilter(browser) \
#         .display_pending_order()
#
#
# def test_display_failed_orders(browser):
#     AdminPage(browser) \
#         .open_admin_page(browser)
#     SearchFilter(browser) \
#         .display_failed_order()
#
#
# def test_display_on_hold_orders(browser):
#     AdminPage(browser) \
#         .open_admin_page(browser)
#     SearchFilter(browser) \
#         .display_on_hold_order()
#
#
# def test_search_order_by_id(browser):
#     AdminPage(browser) \
#         .open_admin_page(browser)
#     SearchFilter(browser) \
#         .search_order_by_id(id_order='11')
#
#
# def test_go_to_next_and_return_previous_page(browser):
#     AdminPage(browser) \
#         .open_admin_page(browser)
#     SearchFilter(browser) \
#         .go_to_next_previous_page(name_attribute='value')
#
#
# def test_open_details_order(browser):
#     AdminPage(browser) \
#         .open_admin_page(browser) \
#         .open_details_order(value='value')
#
#
# def test_open_details_subscription(browser):
#     AdminPage(browser) \
#         .open_admin_page(browser) \
#         .open_page_subscriptions() \
#         .open_details_subscription(value='value')
