from pyscript import document

def create_order(event=None):
    output = document.getElementById("output")
    output.innerHTML = ""  # clear previous result

    name = document.getElementById("cust_name").value.strip()
    address = document.getElementById("cust_address").value.strip()
    contact = document.getElementById("cust_contact").value.strip()

    menu = {
        "carbonara": ("Carbonara", 79.99),
        "garlic": ("Garlic Bread", 50.00),
        "salad": ("Caesar Salad", 150.00),
        "icedtea": ("Iced Tea", 30.00),
        "water": ("Sparkling Water", 20.00)
    }

    total = 0
    ordered_items = []

    for item_id, (label, price) in menu.items():
        checkbox = document.getElementById(item_id)
        if checkbox.checked:
            ordered_items.append(label)
            total += price

    # validation
    if not name or not address or not contact:
        output.innerHTML = "<p style='color:#ff6666;'>⚠ Please fill in all customer details.</p>"
        return

    if not ordered_items:
        output.innerHTML = "<p style='color:#ff6666;'>⚠ Please select at least one item.</p>"
        return

    # formatted HTML receipt
    message = f"""
    <div class='receipt'>
        <h3>🧾 Order Summary</h3>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Address:</strong> {address}</p>
        <p><strong>Contact:</strong> {contact}</p>
        <p><strong>Items:</strong> {', '.join(ordered_items)}</p>
        <p><strong>Total:</strong> ₱{total:.2f}</p>
    </div>
    """

    output.innerHTML = message
