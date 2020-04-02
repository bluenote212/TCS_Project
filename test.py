import com.atlassian.jira.component.ComponentAccessor
import com.deiser.jira.profields.api.field.FieldService
import com.deiser.jira.profields.api.field.number.NumberField
import com.deiser.jira.profields.api.field.script.ScriptField
import com.deiser.jira.profields.api.value.ValueService
import java.text.NumberFormat

// Configuration
def BUDGET_FIELD_ID = 20
def INCURRED_COST_FIELD_ID = 22

// Components
def fieldService = ComponentAccessor.getOSGiComponentInstanceOfType(FieldService.class)
def valueService = ComponentAccessor.getOSGiComponentInstanceOfType(ValueService.class)
def jiraAuthenticationContext = ComponentAccessor.jiraAuthenticationContext


// Get the fields
def budgetField = fieldService.get(BUDGET_FIELD_ID)
def incurredCostField = fieldService.get(INCURRED_COST_FIELD_ID)

// Get the field values in the current project
def budget = valueService.getValue(project, (NumberField) budgetField) ?: 0
def incurredCost = valueService.getValue(project, (ScriptField) incurredCostField)?:"0"
def incurredCostBigDecimal = new BigDecimal(incurredCost)

// Returns the difference between the budget and the incurred cost
def numberFormat = NumberFormat.getInstance(jiraAuthenticationContext.locale)
numberFormat.maximumFractionDigits = 0
numberFormat.minimumFractionDigits = 0
numberFormat.groupingUsed = false
return numberFormat.format((budget - incurredCostBigDecimal)<0?0:(budget - incurredCostBigDecimal))


import com.atlassian.jira.bc.issue.search.SearchService
import com.atlassian.jira.component.ComponentAccessor
import com.atlassian.jira.jql.builder.JqlQueryBuilder
import com.atlassian.jira.web.bean.PagerFilter


// Components
def searchService = ComponentAccessor.getOSGiComponentInstanceOfType(SearchService.class)
def jiraAuthenticationContext = ComponentAccessor.jiraAuthenticationContext

// Script variables
def loggedInUser = jiraAuthenticationContext.getLoggedInUser()

// Make JQL query
def query = JqlQueryBuilder.newBuilder()
        .where()
        .project(project.id).and()
        .unresolved()
        .buildQuery()

// Returns the issue count
return searchService.search(loggedInUser, query, PagerFilter.unlimitedFilter).results.size()