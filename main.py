
from ticket_service import TicketService
from ticket_type_request import TicketTypeRequest


if __name__ == '__main__':

    ticket_service = TicketService()

    ### Tested Scenarios ###
        # request1 = TicketTypeRequest('ADULT',7)
        # request2 = TicketTypeRequest('CHILD',7)
        # request3 = TicketTypeRequest('INFANT',7)
        # request4 = TicketTypeRequest('ADULT',22)
        
        # Scenario 1: AccountId = 123, ticket_type_requests =[request1,request2,request3] (Happy Path Scenario)
        # ticket_service.purchase_tickets(123,[request1,request2,request3])
        # ticket_service.purchase_tickets(123,[request1,request3])

        # Scenario 2: Check when there's No tickets
        # ticket_service.purchase_tickets(123,[])

        # Scenario 3: AccountId = -1 or NAN or '123', ticket_type_requests =[request1,request2,request3] --> Inavlid Account Id exception
        # ticket_service.purchase_tickets('123',[request1,request2,request3])

        # Scenario 4: AccountId = 123, ticket_type_requests =[request2,request3] --> Invalid exception - Child and Infant tickets cannot be purchased without purchasing an Adult ticket
        # ticket_service.purchase_tickets(123,[request2,request3])

        # Scenario 5: AccountId = 123, ticket_type_requests =[request4] --> Invalid exception - More than 20 tickets can't be purchased at a time (Count of Child/Adult/Infant tickets)
        # ticket_service.purchase_tickets(123,[request4])

    ticket_service.purchase_tickets()
