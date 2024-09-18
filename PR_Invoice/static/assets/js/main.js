        function calculateAmount() {
            let quantities = document.querySelectorAll('.quantity');
            let rates = document.querySelectorAll('.rate');
            let amounts = document.querySelectorAll('.amount');
            let gstValues = document.querySelectorAll('.gst');

            let subtotal = 0;
            let totalGst = 0;

            for (let i = 0; i < quantities.length; i++) {
                let quantity = parseFloat(quantities[i].value) || 0;
                let rate = parseFloat(rates[i].value) || 0;
                let gst = parseFloat(gstValues[i].value) || 0;

                let amount = quantity * rate;
                let gstAmount = amount * (gst / 100);
                totalGst += gstAmount;

                amounts[i].value = (amount).toFixed(2);

                subtotal += amount;
            }

            document.getElementById('subtotal').value = subtotal.toFixed(2);

            // Calculate CGST and SGST as half of the total GST
            let cgst = (totalGst / 2).toFixed(2);
            let sgst = (totalGst / 2).toFixed(2);
            document.getElementById('cgst').value = cgst;
            document.getElementById('sgst').value = sgst;

            // Get TDS, Retention, Advance, and Debit Note values
            let tds = parseFloat(document.getElementById('tds').value) || 0;
            let retention = parseFloat(document.getElementById('retention').value) || 0;
            let advance = parseFloat(document.getElementById('advance').value) || 0;
            let debitNote = parseFloat(document.getElementById('debitNote').value) || 0;

            // Calculate the initial net payable amount before rounding
            let netPayable = subtotal - tds - retention - advance - debitNote + parseFloat(cgst) + parseFloat(sgst);

            // Calculate round-off value (difference between netPayable and its integer part)
            let roundOff = netPayable - Math.floor(netPayable);
            document.getElementById('roundOff').value = roundOff.toFixed(2);

            // Adjust net payable to show only the integer part
            netPayable = Math.floor(netPayable);
            document.getElementById('netPayable').value = netPayable;
        }




        function BtnAdd()
        {
             /*Add Button*/
            var v = $("#TRow").clone().appendTo("#TBody") ;
            $(v).find("input").val('');
            $(v).removeClass("table-data");
            $(v).find("th").first().html($('#TBody tr').length - 1);
        }

        function BtnDel(v)
        {
            /*Delete Button*/
           $(v).parent().parent().remove();
           GetTotal();

            $("#TBody").find("tr").each(
            function(index)
            {
               $(this).find("th").first().html(index);
            }

           );
         }