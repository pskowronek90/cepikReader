%dw 2.0

output application/json

var init = payload.data.attributes.marka distinctBy $
var brands = init
var result = brands map (value, index) -> {
    "brand": value,
    "amount": do {
        var attributes = payload.data.attributes
        ---
        sizeOf(attributes filter ((item) -> item.marka == value))
    }
}

var sortByAmount = (result orderBy $.amount)[-1 to 0]
---
/**
Use Dataweave Playground and eg. https://api.cepik.gov.pl//pojazdy?wojewodztwo=30&data-od=20190101&data-do=20191231
for processing the data 
 */   

sortByAmount