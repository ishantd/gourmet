console.log("CHEKC")
window.ingredients = 1
$("#add-ig").click(function () {
    window.ingredients += 1
    var row = `
        <div class="row ig" id="ig-${window.ingredients}">
            <div class="col-md-2">
                <button class="btn btn-sm del-btn" id="dl-ig-${window.ingredients}" type="button"><i class="fa fa-trash" aria-hidden="true"></i></button>
            </div>
            <div class="col-md-5">
                <input type="text" class="form-control" name="ig_names[]" id="ig-name-${window.ingredients}" placeholder="Ingredient Name">
            </div>

            <div class="col-md-3">
                <input type="text" class="form-control" name="ig_value[]" id="ig-value-${window.ingredients}" placeholder="Ingredient Value">
            </div>

            <div class="col-md-2">
                <input type="text" class="form-control" name="ig_unit[]" id="ig-unit-${window.ingredients}" placeholder="Ingredient Unit">
            </div>


        </div>
    `

    var ig_box = $("#ig-box");
    ig_box.append(row);
});

