class Common:

    class search_filter:
        order_search_button = {'css': '#maai1c60xx > div > div > div > button'}
        order_id_filter = {'css': '#swpu1l7ysz > div > div > div > div > span > span > div > input'}
        order_coupon = {'css': '#avj4ngjsg6 > div > div > div > div > span > span > div > input'}
        drop_down = {'css': '#v279z4fg3a > div > div > div > div > span > span > div > button > span.bp3-button-text'}
        processing = {'css': 'body > div.bp3-portal > div > div > div > div > div > ul > li:nth-child(2) > a > div'}
        completed = {'css': 'body > div.bp3-portal > div > div > div > div > div > ul > li:nth-child(3) > a > div'}
        pending = {'css': 'body > div.bp3-portal > div > div > div > div > div > ul > li:nth-child(4) > a > div'}
        failed = {'css': 'body > div.bp3-portal > div > div > div > div > div > ul > li:nth-child(5) > a > div'}
        on_hold = {'css': 'body > div.bp3-portal > div > div > div > div > div > ul > li:nth-child(6) > a > div'}

    class status:
        status_is = {'css': 'div[data-rowindex=0] [data-colindex=4]'}
        status_is_pending = {'css': '#tablenq2fwu0mxu > div.tableWrap > div > div.tbody > div:nth-child(1) > div:nth-child(5) > div'}

    class id_is:
        order_id = {'css': '#tablenq2fwu0mxu > div.tableWrap > div > div.tbody.no-scroll > div:nth-child(1) > div:nth-child(1) > div'}

    class pagination:
        next_page_button = {'css': 'div.appsmith_widget_nq2fwu0mxu div.t--table-widget-next-page > span'}
        previous_page_button = {'css': 'div.appsmith_widget_nq2fwu0mxu div.t--table-widget-prev-page > span'}
        current_page_number = {'css': 'div.appsmith_widget_nq2fwu0mxu input[type=text]'}
