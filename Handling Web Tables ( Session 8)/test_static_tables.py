from playwright.sync_api import Page, expect


def test_static_tables(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    table = page.locator('table[name="BookTable"] tbody')
    expect(table).to_be_visible()

    # number of rows in the table
    rows = table.locator("tr")  # equals to table[name="BookTable"] tbody tr
    rows_count = rows.count()
    expect(rows).to_have_count(rows_count)
    print(f"number of rows: {rows_count}")

    # number of headers/columns
    headers = table.locator("th")
    headers_count = headers.count()
    expect(headers).to_have_count(headers_count)
    print("------------------------ number of columns ----------------------")
    print(f"number of columns: {headers_count}")

    # read all the data 2nd row of the table
    second_row = rows.nth(2).locator("td")
    second_row_texts = second_row.all_inner_texts()
    print(f"secon row data: {second_row_texts}")
    expect(second_row).to_have_text(["Learn Java", "Mukesh", "Java", "500"])

    print("---------------------------- data of 2nd row ------------------------------")
    for text in second_row_texts:
        print(text)

    # read all the data from the table
    all_rows_data = rows.all()

    print("----------------------- all th rows and columns -------------------------")
    for row in all_rows_data[1:]:
        cols = row.locator("td").all_inner_texts()
        print(cols)

    # booknames whose Author is Mukesh
    print("booknames written by Mukesh")
    for row in all_rows_data[1:]:
        auth = row.locator("td").nth(1).inner_text()
        if auth == "Mukesh":
            bookname = row.locator("td").nth(0).inner_text()
            print(f"--> {bookname}")

    # total of all the books
    print("total of all the books:")
    total_price = 0
    for row in all_rows_data[1:]:
        price = row.locator("td").nth(3).inner_text()
        total_price += int(price)
    print("total price: ", total_price)
