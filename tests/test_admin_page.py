from page_objects import AdminPage, SearchFilter
import pytest


def test_open_home_page(browser):
    AdminPage(browser) \
        .open_admin_page(browser) \
        .check_custom_text_widget_orders()


def test_go_to_subscriptions_page(browser):
    AdminPage(browser) \
        .open_admin_page(browser) \
        .open_page_subscriptions() \
        .check_custom_text_widget_subscriptions()


@pytest.mark.parametrize('execution_number', range(1))
def test_go_to_orders_page(browser, execution_number):
    AdminPage(browser) \
        .open_admin_page(browser) \
        .open_page_subscriptions() \
        .open_page_orders() \
        .check_custom_text_widget_orders()


def test_display_processing_orders(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .display_processing_order()


def test_display_completed_orders(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .display_completed_order()


def test_display_pending_orders(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .display_pending_order()


def test_display_failed_orders(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .display_failed_order()


def test_display_on_hold_orders(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .display_on_hold_order()


def test_search_order_by_id(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .search_order_by_id(id_order='11')


def test_go_to_next_and_return_previous_page(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .go_to_next_previous_page(name_attribute='value')


def test_open_details_order(browser):
    AdminPage(browser) \
        .open_admin_page(browser) \
        .open_details_order(value='value')


def test_open_details_subscription(browser):
    AdminPage(browser) \
        .open_admin_page(browser) \
        .open_page_subscriptions() \
        .open_details_subscription(value='value')
