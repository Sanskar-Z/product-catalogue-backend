Feature: Product catalogue management
  Background:
    Given the following products
      | name             | description       | price | category | available |
      | Eco Water Bottle | Reusable bottle   | 19.99 | Kitchen  | true      |
      | Desk Lamp        | LED desk lamp     | 29.50 | Home     | true      |
      | Trail Backpack   | Hiking backpack   | 49.00 | Outdoor  | false     |

  Scenario: Read a product
    When I read the product named "Eco Water Bottle"
    Then the response should contain "Eco Water Bottle"

  Scenario: Update a product
    When I update the product "Eco Water Bottle" price to 24.99
    Then the response should contain "24.99"

  Scenario: Delete a product
    When I delete the product named "Desk Lamp"
    Then the response should not contain "Desk Lamp"

  Scenario: List all products
    When I list all products
    Then the response should contain "Trail Backpack"

  Scenario: Search products by category
    When I search products by category "Kitchen"
    Then the response should contain "Eco Water Bottle"

  Scenario: Search products by availability
    When I search products by availability "false"
    Then the response should contain "Trail Backpack"

  Scenario: Search products by name
    When I search products by name "Lamp"
    Then the response should contain "Desk Lamp"
