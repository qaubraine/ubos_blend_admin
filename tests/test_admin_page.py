from page_objects import AdminPage, SearchFilter
import pytest


def test_open_home_page(browser):
    AdminPage(browser) \
        .open_admin_page(browser) \
        .check_custom_text_widget_benefits()


@pytest.mark.parametrize('execution_number', range(1))
def test_create_new_benefit(browser, execution_number, current_time):
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
                            name=current_time + '+' + str(execution_number), image_name='example_image.png')


def test_delete_last_benefit(browser):
    AdminPage(browser) \
        .open_admin_page(browser) \
        .delete_benefit()

