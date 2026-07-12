from apps.stock.models import StockBatch


def consume_fifo(product, quantity):

    batches = StockBatch.objects.filter(
        product=product,
        remaining_quantity__gt=0
    ).order_by(
        "received_date",
        "id"
    )

    total_stock = sum(
        batch.remaining_quantity
        for batch in batches
    )

    if total_stock < quantity:
        raise ValueError("Stock tidak mencukupi.")

    remaining = quantity
    used_batches = []

    for batch in batches:

        if remaining == 0:
            break

        take = min(
            batch.remaining_quantity,
            remaining
        )

        batch.remaining_quantity -= take
        batch.save(update_fields=["remaining_quantity"])

        used_batches.append({
            "batch_number": batch.batch_number,
            "quantity": take
        })

        remaining -= take

    if remaining > 0:
        raise ValueError("Stock tidak mencukupi.")

    return used_batches